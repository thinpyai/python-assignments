import logging
from logging.config import dictConfig
from datetime import datetime

log_dir = './log'
log_file_path = datetime.now().strftime(f'{log_dir}/log_%Y-%m-%d_%H-%M-%S.log')

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
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': log_file_path,
            'level': logging.DEBUG,
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'encoding': 'utf8'
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
