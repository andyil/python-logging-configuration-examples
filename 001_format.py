import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='[%(name)s]  %(levelname)s %(relativeCreated)d ms %(threadName)s %(message)s')

root = logging.getLogger()
root.debug('hi')
