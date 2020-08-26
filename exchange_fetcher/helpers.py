from django.conf import settings
import requests
import json


def request_exchange_rate():

    api_key = settings.ALPHA_ADVANTAGE_API_KEY
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={api_key}'.format(api_key=api_key)
    data = requests.get(url)
    decoded_data = data.json()
    rate_object = decoded_data["Realtime Currency Exchange Rate"]
    return rate_object


def map_alpa_response_to_exchange_rate_object(response):
    exchange_rate_object = {
        'exchange_rate': response["5. Exchange Rate"],
        'bid_price': response['8. Bid Price'],
        'ask_price': response['9. Ask Price']
    }

    return exchange_rate_object


def get_latest_btc_rates():
    try:
        decoded_response = request_exchange_rate()
        mapped_object = map_alpa_response_to_exchange_rate_object(decoded_response)
    except KeyError:
        return {}

    return mapped_object