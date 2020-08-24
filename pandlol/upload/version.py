import pandas as pd


from logging import getLogger

from pandlol import db
from pandlol.constant import url_versions
from pandlol.utils import log_database_error


logger = getLogger(__name__)  # объект логирования


class Version(db.Model):
    """
    Модель таблицы версий
    """
    __tablename__ = "version_list"

    version_code = db.Column(db.String(20), primary_key=True)

    @classmethod
    @log_database_error(logger)
    def check_version(cls):
        """
        Проверяем загружена ли последняя версия
        """
        df_out = pd.read_json(url_versions)
        df_out.columns = ["version_code"]
        df_in = pd.read_sql_table("version_list", db.engine, index_col=["index"])

        return df_out["version_code"][0] in df_in["version_code"].values

    @classmethod
    @log_database_error(logger)
    def upload(cls):
        """
        Считываем в таблицу версии
        """
        df_out = pd.read_json(url_versions)
        df_out.columns = ["version_code"]

        df_out.to_sql("version_list", db.engine, if_exists="replace")
