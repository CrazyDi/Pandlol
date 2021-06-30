import pandas as pd

from flask_restful import Resource, reqparse

from pandlol.resources.champion_list import champion_list_parser
from pandlol.models.event_skill import EventSkill
from pandlol.utils.data_format import data_order, data_paginate


class ChampionEventSkill(Resource):
    def get(self):
        # Параметры
        param_list = champion_list_parser.parse_args()

        request_params = dict()

        # формируем список параметров
        for key, item in param_list.items():
            if item:
                if key in ['patch', 'platform']:
                    request_params[key] = {'$in': item.split(',')}
                elif key in ['queue', 'tier', 'division']:
                    request_params[key] = {'$in': [int(i) for i in item.split(',')]}

        event_skill = EventSkill(request_params=request_params)
        result_df = event_skill.skill_list()

        # сортировка
        if param_list.get("order"):
            result_df = data_order(result_df, sorted(param_list.get("order")))

        result_data = result_df.to_dict("records")

        # информация о странице
        if param_list.get("page"):
            result_data = data_paginate(result_data, param_list.get("page"))

        result = {
            "status": "OK",
            "data": result_data,
            "total": result_df.shape[0]
        }

        return result, 200
