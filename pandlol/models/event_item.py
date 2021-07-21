import pandas as pd
import requests

from typing import Dict

from pandlol.models.base_model import BaseModel


class EventItem(BaseModel):
    """
    Champion items from the match
    """
    def __init__(self, request_params: Dict):
        super().__init__(table_name="event_item", request_params=request_params)

    def item_list(self):
        item_json = requests.get('http://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/item.json').json()
        df_item = pd.DataFrame(item_json['data']).transpose().reset_index().rename(columns={'index': 'item_id'})
        df_item = df_item[df_item.into.isna()]
        df_item = df_item[df_item['from'].notna()]
        item_list = list(df_item.item_id)
        item_list = [int(i) for i in item_list if int(i) > 3000]

        df = pd.DataFrame(list(self.table.find(self.params)))
        df = df[df.item_id.isin(item_list)]

        df["level"] = df.groupby(["match_id", "champion_name"])["timestamp"].rank("dense")

        df = df[["_id", "champion_name", "item_id", "level"]]

        df_group = df.groupby(["champion_name", "item_id", "level"]).count().reset_index().rename(
            columns={"_id": "count_level"})
        df_sum = df.groupby(["champion_name", "level"]).count().reset_index().rename(
            columns={"_id": "sum_level"}).drop(columns=["item_id"])

        df_all = df_group.merge(df_sum, on=["champion_name", "level"])
        df_all["percent_level"] = round(df_all["count_level"] / df_all["sum_level"] * 100)

        return df_all[df_all["percent_level"] > 0]
