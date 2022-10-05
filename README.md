## My Idea
My main idea of how to achieve this aim is that use a third party API to scrape data from Google Trends, and develop three different scripts to get weekly, daily and hourly data with the keywork 'bitcoin' from 2015-01-01 and save as a csv file. 

## Time I Spent
About three hours, I spend the first two hours to learn about the API I decided to use, and write the major part of scripts, and rest time to polish my code.

## Different Ways I Tried
First I was thinking about use the Beautifulsoup to do data collecting, but I did a bit mroe research and learned about the API I'm using called pytrends.

## The Reasons of Settling on the Current Approach
I learned about that pytrends is a third party API to collect data from Google Trends, and it has built-in functions to do hourly data collection, and weekly for past five years, also, there is a library called dailydata to do daily data collection. So I chose this method to solve this problem. This major difficuly is how to do weekly data collection, because the function was weekly for past five years but 2015 is 7 years ago from now. So I have to create a function to gain data before 2017, and merge them. Finally I achieve all three goals successfully.

## How to Execute My Program
First install pytrends, run <br>
`pip install pytrends` <br>
and then run python files to get different data and they will be saved in different cvs files. Because the hourly data is huge and I recommand to do scraping year by year, and merge them at last. Also, I append weekly and daily data I got, and hourly data of 2015.
