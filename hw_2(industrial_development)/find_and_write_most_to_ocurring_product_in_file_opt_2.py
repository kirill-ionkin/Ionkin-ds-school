import collections
import json
import typing as tp


from load_data_and_create_list_of_product_ids_opt import (
    load_data,
    create_list_of_product_ids,
)
from pairwise_counter_opt import PairwiseCounter


@profile
def find_and_write_most_to_ocurring_product_in_file_2(
    product_ids, pairwise_counter, N=100
):
    MAX_TOP_CANDIDATES: int = 10
    most_co_occurring_products: tp.Dict[str, tp.List[str]] = dict()

    for i in range(N):
        key_1 = product_ids[i]
        candidates: tp.List[tp.Tuple[str, float]] = []

        for j in range(N):
            key_2 = product_ids[j]

            if i == j:
                continue
            if i < j:
                pmi = pairwise_counter.calculate_pmi(key_1, key_2)
            elif i > j:
                pmi = most_co_occurring_products[key_2][i - 1][1]
            candidates.append((key_2, pmi))

        most_co_occurring_products[key_1] = candidates

    for key_i in most_co_occurring_products:
        top_candidates = sorted(
            [elem for elem in most_co_occurring_products[key_i] if elem[1] is not None],
            key=lambda elem: elem[1],
            reverse=True,
        )[:MAX_TOP_CANDIDATES]

        most_co_occurring_products[key_i] = [
            product_id for product_id, pmi in top_candidates
        ]

    with open("most_co_occurring_products_opt.txt", "w") as outfile:
        json.dump(most_co_occurring_products, outfile)


if __name__ == "__main__":
    pairwise_counter = load_data()
    product_ids = create_list_of_product_ids(pairwise_counter)
    find_and_write_most_to_ocurring_product_in_file_2(product_ids, pairwise_counter)
