import pandas as pd

from flask_restful import Resource, reqparse

from pandlol import mongo_db
from pandlol.constant import URL_VERSION, URL_CHAMPION


champion_list_parser = reqparse.RequestParser()
champion_list_parser.add_argument("patch")
champion_list_parser.add_argument("platform")
champion_list_parser.add_argument("queue")
champion_list_parser.add_argument("tier")
champion_list_parser.add_argument("division")


class ChampionList(Resource):
    def get(self):
        # Параметры
        data = champion_list_parser.parse_args()

        request_params = dict()

        # формируем список параметров
        for key, item in data.items():
            if item:
                if key in ['patch', 'platform']:
                    request_params[key] = {'$in': item.split(',')}
                else:
                    request_params[key] = {'$in': [int(i) for i in item.split(',')]}

        # запрос в базу по матчам
        df = pd.DataFrame(list(mongo_db.db.match_detail.find(request_params)))

        # последняя версия
        df_version = pd.read_json(URL_VERSION)

        # список чемпионов
        df_champion_list = pd.read_json(URL_CHAMPION.format(df_version[0][0]))
        df_champion_list = pd.DataFrame(df_champion_list["data"].index)
        df_champion_list.rename(columns={0: "name"})

        # pick rate
        df.groupby("")

        result_data = []

        result = {
            "status": "OK",
            "data": result_data
        }

        return result, 200
