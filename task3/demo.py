import time
from currency_getter import get_currency, SimpleCacheValue

value = SimpleCacheValue(get_currency, 3)

print(value.get_value())
time.sleep(1)
print(value.get_value())
time.sleep(3)
print(value.get_value())