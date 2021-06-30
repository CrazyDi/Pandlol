import pandas as pd

from flask_restful import Resource, reqparse

from pandlol.constant import URL_VERSION, URL_CHAMPION
from pandlol.models.match_list import MatchList
from pandlol.utils.data_format import data_order, data_paginate
from pandlol.utils.custom_exception import ErrorPageParam, ErrorOrderParam


champion_list_parser = reqparse.RequestParser()
champion_list_parser.add_argument("patch")
champion_list_parser.add_argument("platform")
champion_list_parser.add_argument("queue")
champion_list_parser.add_argument("tier")
champion_list_parser.add_argument("division")
champion_list_parser.add_argument("page")
champion_list_parser.add_argument("order", action="append")


class ChampionList(Resource):
    def get(self):
        try:
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

            request_params['early_surr'] = False

            # последняя версия
            df_version = pd.read_json(URL_VERSION)

            # список чемпионов
            df_champion_list = pd.DataFrame(pd.read_json(URL_CHAMPION.format(df_version[0][0])).index).\
                rename(columns={0: "name"}).\
                set_index("name")

            match_list = MatchList(request_params)

            # количество всего выбранных игр
            match_count = round(match_list.count() / 10)

            # pick rate
            df_pick = match_list.champion_list('pick')

            # ban rate
            df_ban = match_list.champion_list('ban')

            # win rate
            request_params['win'] = True
            df_win = match_list.champion_list('win')

            # формируем список чемпионов
            df_champion_list = df_champion_list.join(df_pick).join(df_ban).join(df_win)
            df_champion_list['pick_rate'] = round(df_champion_list['pick'] / match_count * 100, 2)
            df_champion_list['ban_rate'] = round(df_champion_list['ban'] / match_count * 100, 2)
            df_champion_list['win_rate'] = round(df_champion_list['win'] / df_champion_list['pick'] * 100, 2)
            df_champion_list.drop(columns=['pick', 'ban', 'win'], inplace=True)

            result_df = df_champion_list.reset_index()

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
        except ErrorPageParam:
            result = {
                "status": "INTERNAL ERROR",
                "error": "wrong page param"
            }

            return result, 503
        except ErrorOrderParam:
            result = {
                "status": "INTERNAL ERROR",
                "error": "wrong order param"
            }

            return result, 503
        except Exception as e:
            result = {
                "status": "INTERNAL ERROR",
                "error": str(e)
            }

            return result, 503
