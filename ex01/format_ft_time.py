from datetime import datetime

dt = datetime.now()
ts = dt.timestamp()

formatted_ts = f'{ts:,.4f}'
scientific_ts = f'{ts:.2e}'
readable_date = dt.strftime('%b %d %Y')


print(f'Seconds since January 1, 1970: {formatted_ts} or {scientific_ts}\n{readable_date}')