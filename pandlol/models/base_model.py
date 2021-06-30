import pandas as pd

from flask_pymongo.wrappers import Collection
from typing import Dict

from pandlol import mongo_db


class BaseModel:
    """
    Базовая модель запроса данных
    """
    table: Collection = None

    def __init__(self, table_name: str, request_params: Dict):
        self.table = mongo_db.db.get_collection(table_name)
        self.params = request_params

    def count(self):
        """
        Количество записей в таблице
        """
        return self.table.find(self.params).count()

    def data(self) -> pd.DataFrame:
        """
        Данные по параметрам
        :return: Данные
        """
        return pd.DataFrame(list(self.table.find(self.params)))
