![](https://img.shields.io/endpoint?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Falext234%2Fcoronavirus-news%2Fmaster%2Fdata%2Fdata_stats.json)

**NOTE**: scrapper paused on 14 June due to a broken library. To resume once it is fixed.

## coronavirus-news

This repository is an automated bot that scrape news headlines and track if they are related to corona-virus.

Code is executed on schedule with Github Actions. Once completed, it will commit back to the repo chart and data.

Another related repository is https://github.com/alext234/coronavirus-stats for cases statistics.

&#8204;


## Google News
### Chart 

News headlines from all google news domains (most countries and languages) are scraped hourly. 

Below is the cumulative number of news headlines mentioning corona virus related keywords.

![](images/google-news-headlines.png?raw=true)


## Pipeline status
![Run notebooks and commit back](https://github.com/alext234/coronavirus-news/workflows/Run%20notebooks%20and%20commit%20back/badge.svg?branch=master)
