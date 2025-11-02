class Config:
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    SRVER_NAME = "0.0.0.0:8888"

class DevelopmentConfig(Config):
    DEBUG = True
    SRVER_NAME = "0.0.0.0"
    PORT = 3333
