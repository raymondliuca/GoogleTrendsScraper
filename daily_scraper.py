from pytrends.request import TrendReq
from pytrends import dailydata

pytrends = TrendReq(hl='en-US', tz=360) 

kw_list = ['bitcoin']
pytrends.build_payload(kw_list, cat=0, timeframe='2015-01-01 2022-09-30') 

daily_df = dailydata.get_daily_data('bitcoin', 2015, 1, 2015, 2)
print(daily_df)
daily_df.to_csv('daily.csv')