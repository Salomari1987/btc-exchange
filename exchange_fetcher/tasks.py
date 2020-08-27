from celery.schedules import crontab
from btcexchange.celery import periodic_task

from .helpers import get_latest_btc_rates
from .models import ExchangeRate
import logging

logger = logging.getLogger(__name__)


@periodic_task(
    run_every=(crontab(minute=0, hour=1)),
    name='refresh_rate'
)
def refresh_rate():
    latest_rate = get_latest_btc_rates()

    new_obj = ExchangeRate.objects.create(exchange_rate=latest_rate["exchange_rate"], bid_price=latest_rate["bid_price"],ask_price=latest_rate["ask_price"])

    logger.info("object created with id {id}".format(id=new_obj.id))
