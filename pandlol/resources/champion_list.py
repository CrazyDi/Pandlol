import pandas as pd

from flask_restful import Resource, reqparse

from pandlol import mongo_db


champion_list_parser = reqparse.RequestParser()
champion_list_parser.add_argument("patch", type=str, action='split')
champion_list_parser.add_argument("platform", action='split')
champion_list_parser.add_argument("queue", action='split')
champion_list_parser.add_argument("tier", action='split')
champion_list_parser.add_argument("division", action='split')


class ChampionList(Resource):
    def get(self):
        # Параметры
        data = champion_list_parser.parse_args()

        request_params = dict()

        for key, item in data.items():
            if item:
                request_params[key] = {'$in': item}

        df = pd.DataFrame(list(mongo_db.db.match_detail.find({
            'patch':
                {
                    '$in': ['11.8', '11.9', '11.10']
                },
            'platform':
                {
                    '$in': ['RU']
                 },
            'queue':
                {
                    '$in': [420, 440]
                }
        })))

        print(df.shape)

        return request_params, 200
