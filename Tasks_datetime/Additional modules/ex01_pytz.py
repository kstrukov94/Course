from datetime import datetime as dt
import pytz

kld_tz = pytz.timezone("Europe/Kaliningrad")
# date_kld = dt.now(tz=kld_tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
date_UTC = dt.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S %Z%z')
# print(date_kld)
print(date_UTC)


nsk_tz = pytz.timezone("Asia/Novosibirsk")
# date_nsk = dt.now(tz=kld_tz).astimezone(nsk_tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
date_nsk = dt.strptime(date_UTC, '%Y-%m-%d %H:%M:%S %Z%z').astimezone(nsk_tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
print(date_nsk)

