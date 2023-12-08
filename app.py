from flask import Flask
from extensions import db, migrate,ma
import click
from flask.cli import with_appcontext
import os

from views import usuarios_bp

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
DATABASE = os.path.join(basedir, 'instance', 'tutoria_sos.db')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutoria_sos.db' 

db.init_app(app)
migrate.init_app(app,db)
ma.init_app(app)

app.register_blueprint(usuarios_bp)

@click.command(name='init-db')
@with_appcontext
def init_db():
    db.create_all()
    print("base de datos init")
 

app.cli.add_command(init_db)


if __name__ == '__main__':
    app.run(debug=True)