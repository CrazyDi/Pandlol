from pandas import read_json

from logging import getLogger

from pandlol.constant import url_versions
from pandlol.models.version import Version
from pandlol.utils import log_database_error


logger = getLogger(__name__)  # объект логирования


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
        return read_json(url_versions)[0][0] == Version.current_version().version_code

    @classmethod
    @log_database_error(logger)
    def upload(cls):
        """
        Считываем в таблицу версии
        """
        upload_version = Version(0, read_json(url_versions)[0][0])
        upload_version.save_to_db()
