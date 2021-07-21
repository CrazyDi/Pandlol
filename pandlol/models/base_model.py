import pandas as pd

from flask_pymongo.wrappers import Collection
from typing import Dict

from pandlol import mongo_db


class BaseModel:
    """
    Base model access to data
    """
    table: Collection = None

    def __init__(self, table_name: str, request_params: Dict):
        self.table = mongo_db.db.get_collection(table_name)
        self.params = request_params

    def count(self):
        """
        Count of records in the table
        """
        return self.table.find(self.params).count()

    def data(self) -> pd.DataFrame:
        """
        Data with parameters
        :return: Data Frame
        """
        return pd.DataFrame(list(self.table.find(self.params)))
