import pandas as pd

from typing import List, Dict

from pandlol.utils.custom_exception import ErrorOrderParam, ErrorPageParam


def data_order(data: pd.DataFrame, order_list: List):
    """
    Order data by parameters
    :param data: Data for order
    :param order_list: Parameters for order
    :return: Ordered data
    """
    try:
        order_columns = [order.split(",")[1] for order in order_list]
        order_ascending = [order.split(",")[2] == "asc" for order in order_list]

        return data.sort_values(by=order_columns, ascending=order_ascending)
    except Exception:
        raise ErrorOrderParam


def data_paginate(data: List, page: str):
    """
    Return exact page from data
    :param data: Data
    :param page: Page number
    :return: Page of data
    """
    try:
        page_num = int(page.split(",")[0])
        page_size = int(page.split(",")[1])

        return data[((page_num - 1) * page_size):(page_num * page_size)]
    except Exception:
        raise ErrorPageParam


def data_format(df: pd.DataFrame, param_list: Dict):
    """
    Format data by parameters
    :param df: Data
    :param param_list: Parameters
    :return: Formatted data
    """
    # sort
    if param_list.get("order"):
        df = data_order(df, sorted(param_list.get("order")))

    df = df.to_dict("records")

    # paginate
    if param_list.get("page"):
        df = data_paginate(df, param_list.get("page"))

    return df
