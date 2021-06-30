import pandas as pd

from typing import Dict

from pandlol.models.base_model import BaseModel


class MatchList(BaseModel):
    """
    Объект списка матчей
    """
    def __init__(self, request_params: Dict):
        super().__init__(table_name="match_detail", request_params=request_params)

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
