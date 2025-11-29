from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar o banco
    db.init_app(app)

    # Importar models
    from app.models import Professor

    # Registrar blueprint
    from app.main.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Criar tabelas
    with app.app_context():
        db.create_all()

    return app
