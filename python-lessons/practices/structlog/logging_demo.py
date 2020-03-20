# encoding: utf-8
from datetime import datetime
# http://www.structlog.org/en/stable/examples.html
import structlog
from structlog import get_logger

"""
# structlog Intro
- how to use it
- demos
"""

# log = get_logger()
# log.info("key value logging", effect=0, outbox="test")
# log = log.bind(user="hynek", another_key=42)
# log.info("user.logged_in", happy=True)

"""
## 使用structlog和colorama
使用colorama包，可以让打出的日志在终端显示不同的颜色

"""
def add_timestamp(_, __, event_dict):
    event_dict["timestamp"] = datetime.now().isoformat()
    return event_dict


structlog.configure(
    processors=[
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(),
        structlog.dev.ConsoleRenderer(),
        add_timestamp,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.BoundLogger,
    context_class=dict,  # or OrderedDict if the runtime's dict is unordered (e.g. Python <3.6)
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=False
)

log = structlog.get_logger()

log.info("key value logging", effect=0, outbox="test")
log = log.bind(user="hynek", another_key=42)
log.info("user.logged_in", happy=True)

"""
## Logging with context
web application record by log_closure
"""


def view(request):
    user_agent = request.get("HTTP_USER_AGENT", "UNKNOWN")
    peer_ip = request.client_addr
    in_blacklist = True
    if in_blacklist:
        log.msg("something", user_agent=user_agent, peer_ip=peer_ip)
        return "something"
    elif in_blacklist:
        log.msg("something_else", user_agent=user_agent, peer_ip=peer_ip)
        return "something_else"
    else:
        log.msg("else", user_agent=user_agent, peer_ip=peer_ip)
        return "else"


def new_view(request):
    logger = log.bind(
        user_agent=request.get("HTTP_USER_AGENT", "UNKNOWN"),
        peer_ip=request.client_ip
    )
    foo = request.get("foo")
    if foo:
        recorder = logger.bind(foo=foo)



