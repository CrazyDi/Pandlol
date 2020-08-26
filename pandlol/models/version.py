from datetime import datetime
from logging import getLogger

from pandlol import db
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

    @classmethod
    def current_version(cls):
        """
        Получение текущей загруженной версии из БД
        """
        try:
            return cls.query.get(0) or cls(0, "")
        except:
            logger.exception("Exception occurred in func current_version")
            return None

    @log_database_error(logger)
    def save_to_db(self):
        """
        Сохранение записи в БД
        """
        db.session.add(self)
        db.session.commit()
        return None
