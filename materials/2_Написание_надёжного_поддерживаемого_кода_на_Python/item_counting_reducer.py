# -*- coding: utf-8 -*-
import collections
import json


def find_items_most_frequently_puchased_by_user(user_id, records, n_most_frequent):
    """
    По истории заказов определить топ самых частых товаров пользователя.
    Вернуть как идентификаторы этих товаров, так и соответствующие количества.

    :param user_id: Идентификатор пользователя

    :param records: JSON-записи, схема которых содержит 'purchased_items'
    -- список заказов, каждый из которых представляет собой список товаров.

    :param n_most_frequent: Сколько самых популярных товаров отобрать.

    :return: n_most_frequent JSON-записей со схемой ['user_id',
    'top_items'], где top_items -- список словарей, каждый из которых
    имеет схему ['item_id', 'times_purchased']
    """

    # Python-словарь, который в качестве значения хранит
    # количество вхождений ключа в данные.
    item_counter = collections.Counter()
    for record in records:
        # Записи передают в json-формате (обычно сжатом),
        # т.к. он самый простой и универсальный. Следовательно,
        # записи вначале нужно распаковать обратно в Python-словарь.
        unpacked_record = json.loads(record)
        for item_id in unpacked_record["purchased_items"]:
            item_counter[item_id] += 1

    # Метод most_common позволяет получить самые частотные товары
    top_items = item_counter.most_common(n_most_frequent)

    # Теперь нужно сформировать запись и запаковать её обратно в JSON.
    # Т.к. обработка данных потоковая, нужно возвращать записи по мере
    # готовности. Это позволяет обрабатывать группы с разными user_id
    # независимо друг от друга (как и должно быть по смыслу). Такие
    # функции в Python принято называть генераторами.
    yield json.dumps(
        dict(
            user_id=user_id,
            top_items=[
                dict(item_id=item_id, times_purchased=times_purchased)
                for item_id, times_purchased in top_items
            ],
        )
    )
