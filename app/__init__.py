from flask import Flask
from app.extensions import db,migrate
from flask_migrate import Migrate
from app.extensions import migrate, db
from app.controllers.auth.product_controller import store

# application factory function

def create_app():
    
    #app instance
    app = Flask(__name__)
    app.config.from_object('config.Config')


    db.init_app(app)
    migrate.init_app(app,db)
    
    from app.models.product import Product



    @app.route("/")
    def home():
        return "Python Exam"
    

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



