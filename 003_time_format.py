import logging
]import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, datefmt='%H:%M:%S', format='[%(name)s]  %(levelname)s %(asctime)s %(threadName)s %(message)s')

root = logging.getLogger()

root.info('It works')