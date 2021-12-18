__all__ = (
    'currency_getter',
)

import time
import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen
from decimal import Decimal

URL = "http://www.cbr.ru/scripts/XML_daily.asp"

class SimpleCacheValue:
    _cached_value = None
    _expires_at = None
    _ttl = None
    _value_getter = None
    
    def __init__(self, value_getter, ttl):
        self._value_getter = value_getter
        self._ttl = ttl
    
    def get_value(self, *args, **kwargs):
        if not self._expires_at or time.time() >= self._expires_at:
            print("Refreshed")
            self._cached_value = self._value_getter(*args, **kwargs)
            self._expires_at = time.time() + self._ttl
        
        return self._cached_value

    def refresh_value(self, *args, **kwargs):
        self._expires_at = None
        return self.get_value(*args, **kwargs)

def get_currency():
    return_data = {
        'USD': None,
        'EUR': None,
    }
    httprequest = Request(
        URL, method='GET', headers={"Accept": "application/json"}
    )
    with urlopen(httprequest) as httpresponse:
        data = ET.fromstring(
            httpresponse.read().decode(
                httpresponse.headers.get_content_charset("utf-8")
            )
        )
        for valute in data:
            currency = valute.find('CharCode').text
            if currency in return_data.keys():
                return_data[currency] = Decimal(valute.find('Value').text.replace(',', '.'))

    return return_data
