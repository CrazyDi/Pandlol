import pandas as pd

from flask_restful import Resource, reqparse

from pandlol.constant import URL_VERSION, URL_CHAMPION
from pandlol.models.match_list import MatchList
from pandlol.models.event_skill import EventSkill
from pandlol.utils.data_format import data_format
from pandlol.utils.custom_exception import ErrorPageParam, ErrorOrderParam


champion_parser = reqparse.RequestParser()
champion_parser.add_argument("patch")
champion_parser.add_argument("platform")
champion_parser.add_argument("queue")
champion_parser.add_argument("tier")
champion_parser.add_argument("division")
champion_parser.add_argument("position")
champion_parser.add_argument("champion")
champion_parser.add_argument("page")
champion_parser.add_argument("order", action="append")


def parse_params(param_list):
    params = dict()

    # create list of parameters
    for key, item in param_list.items():
        if item:
            if key in ['queue', 'tier', 'division']:
                params[key] = {'$in': [int(i) for i in item.split(',')]}
            elif key == 'position':
                params['position_team'] = {'$in': item.split(',')}
            elif key == "champion":
                params["champion_name"] = item
            elif key in ['order', 'page']:
                pass
            else:
                params[key] = {'$in': item.split(',')}

    # params['early_surr'] = False

    return params


class ChampionList(Resource):
    def get(self):
        """
        Create a new user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - name
              properties:
                email:
                  type: string
                  description: email for user
                name:
                  type: string
                  description: name for user
                address:
                  description: address for user
                  schema:
                    id: Address
                    properties:
                      street:
                        type: string
                      state:
                        type: string
                      country:
                        type: string
                      postalcode:
                        type: string
                groups:
                  type: array
                  description: list of groups
                  items:
                    $ref: "#/definitions/Group"
        responses:
          201:
            description: User created
        """
        try:
            # Parameters
            param_list = champion_parser.parse_args()

            request_params = parse_params(param_list)

            # The last version
            df_version = pd.read_json(URL_VERSION)

            # List of champions
            df_champion_list = pd.DataFrame(pd.read_json(URL_CHAMPION.format(df_version[0][0])).index).\
                rename(columns={0: "name"})

            df_champion_list.replace('Fiddlesticks', 'FiddleSticks', inplace=True)

            df_champion_list.set_index("name", inplace=True)

            match_list = MatchList(request_params)

            # All match count
            match_count = round(match_list.count() / 10)

            # pick rate
            df_pick = match_list.champion_list('pick')

            # ban rate
            df_ban = match_list.champion_list('ban')

            # win rate
            request_params['win'] = True
            df_win = match_list.champion_list('win')

            # Full champion list
            df_champion_list = df_champion_list.join(df_pick).join(df_ban).join(df_win)
            df_champion_list['pick_rate'] = round(df_champion_list['pick'] / match_count * 100, 2)
            df_champion_list['ban_rate'] = round(df_champion_list['ban'] / match_count * 100, 2)
            df_champion_list['win_rate'] = round(df_champion_list['win'] / df_champion_list['pick'] * 100, 2)
            df_champion_list.drop(columns=['pick', 'ban', 'win'], inplace=True)
            df_champion_list.fillna(0, inplace=True)

            if 'position_team' in request_params:
                df_champion_list = df_champion_list[df_champion_list['pick_rate'] > 0]

            result_df = df_champion_list.reset_index()

            result_data = data_format(result_df, param_list)

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


class ChampionEventSkill(Resource):
    def get(self):
        # Parameters
        param_list = champion_parser.parse_args()

        request_params = parse_params(param_list)

        event_skill = EventSkill(request_params=request_params)
        result_df = event_skill.skill_list()

        result_data = data_format(result_df, param_list)

        result = {
            "status": "OK",
            "data": result_data,
            "total": result_df.shape[0]
        }

        return result, 200
