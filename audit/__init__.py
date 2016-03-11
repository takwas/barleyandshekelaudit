from flask import Flask 
from config import Config as config

app = Flask(__name__)
app.config.from_object(config)


from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app_manager = Manager(app)
migrate = Migrate(app, db)
app_manager.add_command('db', MigrateCommand)

from . import views#, forms, models


if __name__=='__main__':
    app.run(debug=True)