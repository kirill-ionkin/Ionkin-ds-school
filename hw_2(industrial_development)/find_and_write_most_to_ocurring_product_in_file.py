import collections
import json
import typing as tp

from tqdm.auto import tqdm

from load_data_and_create_list_of_product_ids import (
    load_data,
    create_list_of_product_ids,
)
from pairwise_counter import PairwiseCounter


@profile
def find_and_write_most_to_ocurring_product_in_file(product_ids, pairwise_counter):
    MAX_TOP_CANDIDATES: int = 10
    most_co_occurring_products: tp.Dict[str, tp.List[str]] = dict()

    for key_1 in tqdm(product_ids[:100], desc="outer loop"):
        candidates: tp.List[tp.Tuple[str, float]] = []
        for key_2 in product_ids[:100]:
            if key_1 == key_2:
                continue

            pmi = pairwise_counter.calculate_pmi(key_1, key_2)
            if pmi is None:
                continue

            candidates.append((key_2, pmi))

        top_candidates = sorted(candidates, key=lambda p: p[1], reverse=True)[
            :MAX_TOP_CANDIDATES
        ]
        most_co_occurring_products[key_1] = [
            product_id for product_id, pmi in top_candidates
        ]

    with open("most_co_occurring_products.txt", "w") as outfile:
        json.dump(most_co_occurring_products, outfile)


if __name__ == "__main__":
    pairwise_counter = load_data()
    product_ids = create_list_of_product_ids(pairwise_counter)
    find_and_write_most_to_ocurring_product_in_file(product_ids, pairwise_counter)
