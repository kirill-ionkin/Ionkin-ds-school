import collections
import json
import typing as tp

from tqdm.auto import tqdm

from pairwise_counter import PairwiseCounter


@profile
def load_data():
    with open("product_pairwise_counter.txt", "r", encoding="utf8") as infile:
        pairwise_counter = PairwiseCounter.from_dict(json.load(infile))
    return pairwise_counter


@profile
def create_list_of_product_ids(pairwise_counter):
    product_ids = [
        product_id
        for product_id in pairwise_counter.index_mapper.keys()
        if product_id != pairwise_counter.total_key
    ]
    return product_ids


if __name__ == "__main__":
    pairwise_counter = load_data()
    product_ids = create_list_of_product_ids(pairwise_counter)
