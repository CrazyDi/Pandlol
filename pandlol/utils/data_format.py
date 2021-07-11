import pandas as pd

from typing import List, Dict

from pandlol.utils.custom_exception import ErrorOrderParam, ErrorPageParam


def data_order(data: pd.DataFrame, order_list: List):
    """
    Сортировка по параметрам
    :param data: Массив, который надо сортировать
    :param order_list: Список сортирровки из параметров
    :return: Отсортированный массив
    """
    try:
        order_columns = [order.split(",")[1] for order in order_list]
        order_ascending = [order.split(",")[2] == "asc" for order in order_list]

        return data.sort_values(by=order_columns, ascending=order_ascending)
    except Exception:
        raise ErrorOrderParam


def data_paginate(data: List, page: str):
    """
    Возвращает указанную страницу из данных
    :param data: Данные
    :param page: Страница из параметров
    :return: Страница данных
    """
    try:
        page_num = int(page.split(",")[0])
        page_size = int(page.split(",")[1])

        return data[((page_num - 1) * page_size):(page_num * page_size)]
    except Exception:
        raise ErrorPageParam


def data_format(param_list: Dict, df: pd.DataFrame):
    # сортировка
    if param_list.get("order"):
        df = data_order(df, sorted(param_list.get("order")))

    df = df.to_dict("records")

    # информация о странице
    if param_list.get("page"):
        df = data_paginate(df, param_list.get("page"))

    return df
