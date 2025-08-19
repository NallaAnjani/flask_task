class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/student_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey"
    JWT_SECRET_KEY = "jwt-secret-string"
