import pandas as pd
from datetime import datetime


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

    index = db.Column(db.Integer, primary_key=True, nullable=False)
    version_code = db.Column(db.String(20), unique=True, nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, index, version_code):
        self.version_code = version_code
        self.index = index
        self.upload_date = datetime.utcnow()

    @log_database_error(logger)
    def save_to_db(self):
        """
        Сохранение пользователя в БД
        """
        db.session.add(self)
        db.session.commit()
        return None


class VersionUploader:
    """
    Класс загрузки версий
    """

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
        df_in = pd.read_sql_table("version_list", db.engine, index_col=["index"])

        for index in df_out.index:
            if df_out.version_code[index] not in df_in.version_code.values:
                new_version = Version(index, df_out.version_code[index])
                new_version.save_to_db()
