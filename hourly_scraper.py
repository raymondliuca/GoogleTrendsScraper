from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360) 

kw_list = ['bitcoin']
pytrends.build_payload(kw_list, cat=0, timeframe='2015-01-01 2022-09-30') 

hourly_df_2015 = pytrends.get_historical_interest(kw_list, year_start=2015, month_start=1, day_start=1, hour_start=0, year_end=2015, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2016 = pytrends.get_historical_interest(kw_list, year_start=2016, month_start=1, day_start=1, hour_start=0, year_end=2016, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2017 = pytrends.get_historical_interest(kw_list, year_start=2017, month_start=1, day_start=1, hour_start=0, year_end=2017, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2018 = pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2019 = pytrends.get_historical_interest(kw_list, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2019, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2020 = pytrends.get_historical_interest(kw_list, year_start=2020, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2021 = pytrends.get_historical_interest(kw_list, year_start=2021, month_start=1, day_start=1, hour_start=0, year_end=2021, month_end=12, day_end=31, hour_end=0, cat=0, sleep=0).reset_index()
hourly_df_2022 = pytrends.get_historical_interest(kw_list, year_start=2022, month_start=1, day_start=1, hour_start=0, year_end=2022, month_end=9, day_end=30, hour_end=0, cat=0, sleep=0).reset_index()

frames = [hourly_df_2015, hourly_df_2016, hourly_df_2017, hourly_df_2018, hourly_df_2019, hourly_df_2020, hourly_df_2021, hourly_df_2022]
result = pd.concat(frames)
result.to_csv('hourly.csv')