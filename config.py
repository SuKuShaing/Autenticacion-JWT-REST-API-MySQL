from decouple import config # Función para traer variables de entorno


class Config:
    SECRET_KEY = config("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True


config = {"development": DevelopmentConfig}
