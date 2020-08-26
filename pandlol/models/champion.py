from logging import getLogger

from pandlol import db
from pandlol.utils import log_database_error


logger = getLogger(__name__)  # объект логирования


class Champion(db.Model):
    """
    Модель таблицы чемпионов
    """

    __tablename__ = "champion_list"

    champion_id = db.Column(db.Integer, primary_key=True)
    champion_name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, champion_id, champion_name):
        self.champion_id = champion_id
        self.champion_name = champion_name

    @log_database_error(logger)
    def save_to_db(self):
        """
        Сохранение записи в БД
        """
        db.session.add(self)
        db.session.commit()
        return None
