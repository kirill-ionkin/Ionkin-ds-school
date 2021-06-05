import torch
import torch.nn as nn
import torch.nn.functional as F


class SegmenterModel(nn.Module):
    def __init__(self):
        super(SegmenterModel, self).__init__()
        self.init_ch = 64  # число каналов после первой свёртки
        self.n_levels = 4  # число уровней до "основания" параболы

    # raise NotImplementedError()

    def forward(self, x):
        # raise NotImplementedError()
        pass

    def predict(self, x):
        # на вход подаётся одна картинка, а не батч, поэтому так
        y = self.forward(x.unsqueeze(0).cuda())
        return (y > 0).squeeze(0).squeeze(0).float().cuda()


class Unet(SegmenterModel):
    def __init__(self):
        super(Unet, self).__init__()
        self.sigmoid = nn.Sigmoid()

        # pool, unpool
        self.pool = nn.MaxPool2d(kernel_size=(2, 2), stride=2, return_indices=True)
        self.unpool = nn.MaxUnpool2d(kernel_size=(2, 2))

        # encoder
        self.enc_conv0 = nn.Sequential(
            nn.Conv2d(
                in_channels=3,
                out_channels=64,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=64,
                out_channels=64,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(64),
            nn.ReLU(),
        )

        self.enc_conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=64,
                out_channels=128,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=128,
                out_channels=128,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(128),
            nn.ReLU(),
        )

        self.enc_conv2 = nn.Sequential(
            nn.Conv2d(
                in_channels=128,
                out_channels=256,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=256,
                out_channels=256,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(256),
            nn.ReLU(),
        )

        self.enc_conv3 = nn.Sequential(
            nn.Conv2d(
                in_channels=256,
                out_channels=512,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=512,
                out_channels=512,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(512),
            nn.ReLU(),
        )

        # bottleneck
        self.bottleneck = nn.Sequential(
            nn.Conv2d(
                in_channels=512,
                out_channels=1024,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(1024),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=1024,
                out_channels=1024,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(1024),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=1024,
                out_channels=512,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(512),
            nn.ReLU(),
        )

        # decoder
        self.dec_conv0 = nn.Sequential(
            nn.Conv2d(
                in_channels=1024,
                out_channels=512,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=512,
                out_channels=256,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(256),
            nn.ReLU(),
        )

        self.dec_conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=512,
                out_channels=256,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=256,
                out_channels=128,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(128),
            nn.ReLU(),
        )

        self.dec_conv2 = nn.Sequential(
            nn.Conv2d(
                in_channels=256,
                out_channels=128,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=128,
                out_channels=64,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(64),
            nn.ReLU(),
        )

        self.dec_conv3 = nn.Sequential(
            nn.Conv2d(
                in_channels=128,
                out_channels=64,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=64,
                out_channels=64,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=64,
                out_channels=64,
                kernel_size=(3, 3),
                padding=1,
                padding_mode="reflect",
            ),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=64, out_channels=1, kernel_size=(1, 1)
            ),  # after last conv no activations
        )

    def forward(self, x):
        # encoder
        enc_conv0_output = self.enc_conv0(x)
        e0, indices1 = self.pool(enc_conv0_output)

        enc_conv1_output = self.enc_conv1(e0)
        e1, indices2 = self.pool(enc_conv1_output)

        enc_conv2_output = self.enc_conv2(e1)
        e2, indices3 = self.pool(enc_conv2_output)

        enc_conv3_output = self.enc_conv3(e2)
        e3, indices4 = self.pool(enc_conv3_output)

        # bottleneck
        b = self.bottleneck(e3)

        # decoder
        d0 = self.dec_conv0(
            torch.cat((self.unpool(b, indices4), enc_conv3_output), dim=1)
        )
        d1 = self.dec_conv1(
            torch.cat((self.unpool(d0, indices3), enc_conv2_output), dim=1)
        )
        d2 = self.dec_conv2(
            torch.cat((self.unpool(d1, indices2), enc_conv1_output), dim=1)
        )
        d3 = self.dec_conv3(
            torch.cat((self.unpool(d2, indices1), enc_conv0_output), dim=1)
        )  # no activation

        # d3_activation = self.sigmoid(d3)
        return d3
