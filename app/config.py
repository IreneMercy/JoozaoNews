class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = '87082138d3fc4755892f9c7266f6ceea'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
