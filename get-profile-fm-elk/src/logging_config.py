import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': logging.INFO,
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': './otc-profile/logs/get-profile.log',
            'level': logging.DEBUG,
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': logging.DEBUG,
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': logging.DEBUG,
            'propagate': True
        },
    }
}


def setup_logging():
    """Setup logging
    """
    dictConfig(LOGGING_CONFIG)
