from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from pandlol import app, db

# Объект миграции данных
migrate = Migrate(app, db)

# Менеджер миграции данных
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
