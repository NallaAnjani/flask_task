from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    # Register Blueprints
    from app.routes.students import students_bp
    app.register_blueprint(students_bp, url_prefix="/students")


# from app.routes.students import students_bp
#     from app.routes.subjects import subjects_bp
#     from app.routes.teachers import teachers_bp
#     from app.routes.grades import grades_bp
#     from app.auth import auth_bp

#     app.register_blueprint(students_bp, url_prefix="/students")
#     app.register_blueprint(subjects_bp, url_prefix="/subjects")
#     app.register_blueprint(teachers_bp, url_prefix="/teachers")
#     app.register_blueprint(grades_bp, url_prefix="/grades")
#     app.register_blueprint(auth_bp, url_prefix="/auth")



    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
