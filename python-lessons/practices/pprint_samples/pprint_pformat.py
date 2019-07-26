# -*- coding:utf-8 -*-
import logging
from pprint import pformat, pprint

from pymodules.pprint import data

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s'
)

logging.debug('Logging pformatted data')
formatted = pformat(data)
pprint(formatted)
for line in formatted.splitlines():
    logging.debug(line.rstrip())