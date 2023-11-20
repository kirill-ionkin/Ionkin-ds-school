import collections
import json
import typing as tp

from tqdm.auto import tqdm

from pairwise_counter_opt_v3 import PairwiseCounter


def load_data():
    with open("product_pairwise_counter.txt", "r", encoding="utf8") as infile:
        pairwise_counter = PairwiseCounter.from_dict_wrapper(json.load(infile))
    return pairwise_counter


def create_list_of_product_ids(pairwise_counter):
    return [
        product_id
        for product_id in pairwise_counter.index_mapper.keys()
        if product_id != pairwise_counter.total_key
    ]


if __name__ == "__main__":
    pairwise_counter = load_data()
    product_ids = create_list_of_product_ids(pairwise_counter)
