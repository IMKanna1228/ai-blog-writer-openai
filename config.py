##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
