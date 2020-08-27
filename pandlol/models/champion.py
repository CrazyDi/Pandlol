from logging import getLogger

from pandlol import db
from pandlol.utils import log_database_error


logger = getLogger(__name__)  # объект логирования


class ChampionModel(db.Model):
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

    @classmethod
    @log_database_error(logger)
    def delete_all_from_db(cls):
        """
        Удаление всех записей из таблицы
        """
        cls.query.delete()
        db.session.commit()
        return None


class TagModel(db.Model):
    """
    Модель таблицы тегов
    """
    __tablename__ = "tag_list"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag_name = db.Column(db.String(20), nullable=False, unique=True)

    @classmethod
    @log_database_error(logger)
    def delete_all_from_db(cls):
        """
        Удаление всех записей из таблицы
        """
        cls.query.delete()
        db.session.commit()
        return None


class ChampionTagModel(db.Model):
    """
    Модель таблицы тегов чемпионов
    """
    __tablename__ = "champion_tag"

    champion_tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    champion_id = db.Column(db.Integer, db.ForeignKey('champion_list.champion_id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag_list.tag_id'))

    champion = db.relationship(ChampionModel, backref=db.backref("champion_tag"))
    tag = db.relationship(TagModel, backref=db.backref("champion_tag"))

    @log_database_error(logger)
    def save_to_db(self):
        """
        Сохранение записи в БД
        """
        db.session.add(self)
        db.session.commit()
        return None

    @classmethod
    @log_database_error(logger)
    def delete_all_from_db(cls):
        """
        Удаление всех записей из таблицы
        """
        cls.query.delete()
        db.session.commit()
        return None
