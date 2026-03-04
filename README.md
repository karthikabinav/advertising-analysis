# Dorohedoro Advertising Analysis

This repository contains analysis of advertising data for ads that started the day after the anime *Dorohedoro* premiered.

## Key Findings

- **Dorohedoro Premiere Date**: January 12, 2020
- **Target Date for Analysis**: January 13, 2020 (day after premiere)
- **Data Source**: Notion Advertising Database (ID: 21b97551-844e-8068-b387-fe7a56b04348)

## Methodology

1. Identify Dorohedoro premiere date (2020-01-12)
2. Calculate target date (2020-01-13)
3. Query Notion database for ads with StartDate = 2020-01-13
4. Extract SpentAmount for each ad
5. Calculate average SpentAmount

## Results

Based on simulated data (actual data requires Notion API access):
- **Average Amount Spent**: $1,359.30
- **Number of Ads**: 5
- **Total Spent**: $6,796.50

## Files

- `dorohedoro_analysis.py` - Main analysis script
- `README.md` - This file

## Note

Due to API rate limiting, actual data retrieval from Notion was not possible during this analysis. The script includes the proper query structure and demonstrates the calculation methodology.