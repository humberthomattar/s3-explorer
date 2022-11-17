from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# inicializando o SQLAlchemy
db = SQLAlchemy()
# Objeto para o flask-migrate
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # configuracoes da app
    app.config.from_object('config.DevConfig')
    
    ## registro dos blueprints

    # blueprint da aplicacao principal
    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # blueprint da autenticacao
    from .blueprints.auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    # blueprint da account
    from .blueprints.account.account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/account')

    
    # inicializacao do Banco de Dados
    db.init_app(app)
    migrate.init_app(app, db)    
        
    # LoginManager - Flask-login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models import User
    
    # recuperacao do usuario autenticado
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    return app