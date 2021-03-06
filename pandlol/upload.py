from os import getcwd
from sys import path
path.insert(1, getcwd())

from datetime import datetime
from pandas import read_json, DataFrame, read_sql_table, merge
from logging import getLogger

from pandlol import db
from pandlol.constant import url_versions, url_champions, stat
from pandlol.models.version import VersionModel
from pandlol.models.champion import ChampionModel, TagModel, ChampionTagModel, ChampionStatModel
from pandlol.utils import log_database_error


logger = getLogger(__name__)  # объект логирования


def get_last_version():
    return read_json(url_versions)[0][0]


@log_database_error(logger)
def upload_version(version):
    """
    Считываем в таблицу версии
    """
    current_version = VersionModel.current_version()
    current_version.version_code = version
    current_version.upload_date = datetime.utcnow()
    current_version.save_to_db()


def upload_champion(version):
    """
    Загрузка чемпионов
    """
    # читаем данные и преобразовываем их в нужный вид
    new_df = read_json(url_champions.format(version))["data"].apply(lambda x: x["key"]).reset_index()
    new_df.columns = ["champion_name", "champion_id"]

    # удаляем старые записи
    ChampionStatModel.delete_all_from_db()
    ChampionTagModel.delete_all_from_db()
    ChampionModel.delete_all_from_db()

    # записываем новые записи
    new_df.to_sql("champion_list", db.engine, if_exists="append", index=False)


def upload_tag(version):
    """
    Загрузка тегов
    """
    # читаем данные и преобразовываем их в нужный вид
    tag_set = set()
    read_json(url_champions.format(version))["data"].apply(lambda x: [tag_set.add(y) for y in x["tags"]])
    tag_df = DataFrame({"tag_name": list(tag_set)})

    # удаляем старые записи
    TagModel.delete_all_from_db()

    # записываем новые данные
    tag_df.to_sql("tag_list", db.engine, if_exists="append", index=False)


def upload_champion_tag(version):
    """
    Загрузка тегов чемпионов
    """
    # исходные данные
    champion_df = read_json(url_champions.format(version))["data"]
    tag_df = read_sql_table("tag_list", db.engine)

    # преобразовываем данные в нужный вид
    champion_df = DataFrame(list(champion_df.values))[["key", "tags"]]
    print(champion_df.columns)
    print(tag_df.columns)
    champion_df.columns = ["champion_id", "tags"]
    champion_df = DataFrame(champion_df.tags.tolist(), index=champion_df.champion_id)\
        .stack()\
        .reset_index(level=1, drop=True)\
        .reset_index()
    print(champion_df.columns)
    champion_tag_df = merge(champion_df, tag_df, left_on=0, right_on="tag_name")
    champion_tag_df = champion_tag_df[["champion_id", "tag_id"]]

    # удаляем старые записи
    ChampionTagModel.delete_all_from_db()

    # записываем данные в таблицу
    champion_tag_df.to_sql("champion_tag", db.engine, if_exists="append", index=False)


def upload_champion_stat(version):
    """
    Загрузка статистических показателей чемпионов
    """
    # исходные данные
    champion_df = read_json(url_champions.format(version))["data"]

    # Преобразуем данные
    champion_df = DataFrame(list(champion_df.values))[["key", "stats"]]
    champion_df = DataFrame(list(champion_df.stats), index=champion_df.key)
    champion_df = champion_df.stack().reset_index(level=1).reset_index()
    champion_stat_df = merge(champion_df, stat, left_on="level_1", right_on="stat_name")
    champion_stat_df = champion_stat_df[["key", "stat_code", 0]]
    champion_stat_df.columns = ["champion_id", "stat_code", "stat_value"]

    # удаляем старые записи
    # ChampionStatModel.delete_all_from_db()

    # записываем данные в таблицу
    champion_stat_df.to_sql("champion_stat", db.engine, if_exists="append", index=False)


if __name__ == "__main__":
    # Если последняя версия не загружена
    last_version = get_last_version()
    print(last_version)
    # if not last_version == VersionModel.current_version().version_code:
        # pass
    upload_champion(last_version)
    upload_tag(last_version)
    upload_champion_tag(last_version)
    upload_champion_stat(last_version)
    upload_version(last_version)
