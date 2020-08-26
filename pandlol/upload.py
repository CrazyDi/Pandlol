from os import getcwd
from sys import path
path.insert(1, getcwd())

from pandas import read_json
from logging import getLogger

from pandlol import db
from pandlol.constant import url_versions, url_champions
from pandlol.models.version import VersionModel
from pandlol.models.champion import ChampionModel
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
    current_version.save_to_db()


@log_database_error(logger)
def upload_champion(version):
    """
    Загрузка чемпионов
    """
    # читаем данные и преобразовываем их в нужный вид
    new_df = read_json(url_champions.format(version))["data"].apply(lambda x: x["key"]).reset_index()
    new_df.columns = ["champion_name", "champion_id"]

    # удаляем старые записи
    ChampionModel.delete_all_from_db()

    # записываем новые записи
    new_df.to_sql("champion_list", db.engine, if_exists="append", index=False)


if __name__ == "__main__":
    # Если последняя версия не загружена
    last_version = get_last_version()
    print(last_version)
    if not last_version == VersionModel.current_version().version_code:
        # pass
        upload_champion(last_version)
        upload_version(last_version)
