import os


class Config:
    SECRET_KEY = '2a509b6cc825d66df73ca4df444ef072'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '1f59c487c0cecf'
    MAIL_PASSWORD = '5e5b5fb74a87c8'

