import pandas as pd

from typing import Dict

from pandlol.models.base_model import BaseModel


class EventSkill(BaseModel):
    """
    Объект прокачки скиллов
    """
    def __init__(self, request_params: Dict):
        super().__init__(table_name="event_skill", request_params=request_params)

    def skill_list(self):
        """
        Список прокачки скиллов чемпиона
        :return: Результат
        """
        df = pd.DataFrame(list(self.table.find(self.params)))
        df["rank"] = df.groupby(["match_id", "champion_name"])["timestamp"].rank("dense")

        df = df[["_id", "champion_name", "skill_code", "rank"]]

        df_group = df.groupby(["champion_name", "skill_code", "rank"]).count().reset_index().rename(
            columns={"_id": "count_rank"})
        df_sum = df.groupby(["champion_name", "rank"]).count().reset_index().rename(
            columns={"_id": "sum_rank"}).drop(columns=["skill_code"])

        df_all = df_group.merge(df_sum, on=["champion_name", "rank"])
        df_all["percent_rank"] = round(df_all["count_rank"] / df_all["sum_rank"] * 100)

        return df_all[df_all["percent_rank"] > 0]
