from logging import getLogger
from pandas import read_json

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
    def upload(cls):
        """
        Считываем в таблицу версии
        """
        df = read_json(url_versions)
        df.columns = ["version_code"]
        print(db.engine)

        df.to_sql("version_list", db.engine, if_exists="replace")
