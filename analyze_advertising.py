import requests
import json
from datetime import datetime, timedelta

# Dorohedoro premiered on January 12, 2020
premiere_date = datetime(2020, 1, 12)
day_after = premiere_date + timedelta(days=1)
target_date = day_after.strftime('%Y-%m-%d')

print(f"Dorohedoro premiere date: {premiere_date.strftime('%Y-%m-%d')}")
print(f"Querying ads that started on: {target_date}")
print(f"Database ID: 21b97551-844e-8068-b387-fe7a56b04348")

# This would query the Notion database for ads starting on 2020-01-13
# and calculate the average SpentAmount

# Sample calculation logic:
# 1. Query database with filter: StartDate equals 2020-01-13
# 2. Extract SpentAmount from each result
# 3. Calculate average

print("\nExpected query filter:")
print(json.dumps({
    "property": "StartDate",
    "date": {"equals": target_date}
}, indent=2))

print("\nNote: Actual data retrieval would require Notion API access.")
print("The average SpentAmount would be calculated from the query results.")
