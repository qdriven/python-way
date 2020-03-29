from loguru import logger
logger.debug("that's it, it is ready")
logger.info("that's it, it is ready")
import sys
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("file_{time}.log",rotation="200 MB")
logger.add("file_{time}.log",rotation="12:00")
logger.add("file_{time}.log",rotation="1 week",compression="zip")
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)
my_function(1,2,3)
nested(0)logger.add("somefile.log", enqueue=True)
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
logger.info("log color testing")
# For scripts
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": "file.log", "serialize": True},
    ],
    "extra": {"user": "someone"}
}
logger.configure(**config)

# For libraries
logger.disable("my_library")
logger.info("No matter added sinks, this message is not displayed")
logger.enable("my_library")
logger.info("This message however is propagated to the sinks")

import notifiers

params = {
    "username": "you@gmail.com",
    "password": "abc123",
    "to": "dest@gmail.com"
}

# Send a single notification
notifier = notifiers.get_notifier("gmail")
notifier.notify(message="The application is running!", **params)

# Be alerted on each error message
from notifiers.logging import NotificationHandler

handler = NotificationHandler("gmail", defaults=params)
logger.add(handler, level="ERROR")
logger.info("some error happened")## Define System Environement and Parse the log# Linux / OSX
export LOGURU_FORMAT="{time} | <lvl>{message}</lvl>"

# Windows
setx LOGURU_DEBUG_COLOR "<green>"
pattern = r"(?P<time>.*) - (?P<level>[0-9]+) - (?P<message>.*)"  # Regex with named groups
caster_dict = dict(time=dateutil.parser.parse, level=int)        # Transform matching groups

for groups in logger.parse("file.log", pattern, cast=caster_dict):
    print("Parsed:", groups)
    # {"level": 30, "message": "Log example", "time": datetime(2018, 12, 09, 11, 23, 55)}