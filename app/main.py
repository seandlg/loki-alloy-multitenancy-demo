import logging
from time import sleep
import datetime

logger = logging.getLogger("app_logger")
tenant_logger = logging.getLogger("tenant_logger")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
)
logging.Formatter.formatTime = (  # type: ignore[assignment]
    lambda self, record, datefmt=None: datetime.datetime.fromtimestamp(
        record.created, datetime.timezone.utc
    )
    .astimezone()
    .isoformat(sep="T", timespec="microseconds")
)  # // ISO 8601 format with microseconds and timezone


while True:
    sleep_time = 0.5
    logger.info("log1")
    sleep(sleep_time)
    tenant_logger.info("tenant1")
    sleep(sleep_time)
    logger.info("log2")
    sleep(sleep_time)
    tenant_logger.info("tenant2")
    sleep(sleep_time)
