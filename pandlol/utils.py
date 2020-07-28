import functools

from sqlalchemy.exc import IntegrityError, DataError, DatabaseError, InterfaceError


def log_database_error(logger):
    """
    Декоратор для обработки ошибок БД
    """
    def decorated(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IntegrityError as e:
                logger.exception("Exception {} occurred in func {}".format(e.orig.pgcode, func.__name__))
                return e.orig.pgcode
            except DataError as e:
                logger.exception("Exception {} occurred in func {}".format(e.orig.pgcode, func.__name__))
                return e.orig.pgcode
            except DatabaseError as e:
                logger.exception("Exception {} occurred in func {}".format(e.orig.pgcode, func.__name__))
                return e.orig.pgcode
            except InterfaceError as e:
                logger.exception("Exception {} occurred in func {}".format(e.orig.pgcode, func.__name__))
                return e.orig.pgcode
            except:
                logger.exception("Unknown exception occurred in func {}".format(func.__name__))
                return '-1000'
        return wrapped
    return decorated
