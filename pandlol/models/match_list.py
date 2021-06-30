import pandas as pd

from flask_pymongo.wrappers import Collection
from typing import Dict

from pandlol import mongo_db


class MatchList:
    """
    Объект списка матчей
    """
    table: Collection = None

    def __init__(self, request_params: Dict):
        self.table = mongo_db.db.match_detail
        self.params = request_params

    def count(self):
        """
        Количество записей в таблице
        """
        return self.table.find(self.params).count()

    def champion_list(self, request: str):
        """
        Список чемпионов с указанным параметром
        :param request: Pick, Ban, Win
        :return: pd.DataFrame
        """
        field_name = '$_id'
        if request in ['pick', 'win']:
            field_name = '$champion_pick'
        elif request == 'ban':
            field_name = '$champion_ban'

        return pd.DataFrame(list(self.table.aggregate([
            {
                '$match': self.params,
            },
            {
                '$group':
                    {
                        '_id': field_name,
                        'count':
                            {
                                '$sum': 1
                            }
                    }
            }
        ]))).rename(columns={"_id": "name", "count": request}).set_index("name")
