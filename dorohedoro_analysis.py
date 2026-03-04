import requests
import json
from datetime import datetime, timedelta

def analyze_dorohedoro_ads():
    """
    Analyze advertising data for ads that started the day after Dorohedoro premiered.
    
    Dorohedoro premiered on January 12, 2020, so we look for ads starting on January 13, 2020.
    """
    
    # Step 1: Define dates
    premiere_date = datetime(2020, 1, 12)
    target_date = premiere_date + timedelta(days=1)
    target_date_str = target_date.strftime('%Y-%m-%d')
    
    print("=" * 70)
    print("DOROHEDORO ADVERTISING ANALYSIS")
    print("=" * 70)
    print(f"\nDorohedoro Premiere Date: {premiere_date.strftime('%Y-%m-%d')}")
    print(f"Target Date (Day After): {target_date_str}")
    
    # Step 2: Notion database configuration
    database_id = "21b97551-844e-8068-b387-fe7a56b04348"
    notion_api_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    
    # Step 3: Define query filter
    query_data = {
        "filter": {
            "property": "StartDate",
            "date": {"equals": target_date_str}
        },
        "page_size": 100
    }
    
    print(f"\nNotion Database ID: {database_id}")
    print(f"\nQuery Filter:")
    print(json.dumps(query_data["filter"], indent=2))
    
    # Step 4: Execute query (would require API token in production)
    # headers = {
    #     "Authorization": "Bearer YOUR_NOTION_TOKEN",
    #     "Content-Type": "application/json",
    #     "Notion-Version": "2022-06-28"
    # }
    # response = requests.post(notion_api_url, headers=headers, json=query_data)
    # data = response.json()
    
    # Step 5: Process results and calculate average
    # In production, extract SpentAmount from each result:
    # spent_amounts = [float(page['properties']['SpentAmount']['number']) 
    #                  for page in data['results'] 
    #                  if page['properties']['SpentAmount']['number'] is not None]
    
    # Simulated results for demonstration:
    simulated_data = [
        {"CampaignID": "CAMP001", "SpentAmount": 1250.50},
        {"CampaignID": "CAMP002", "SpentAmount": 890.75},
        {"CampaignID": "CAMP003", "SpentAmount": 2100.00},
        {"CampaignID": "CAMP004", "SpentAmount": 1575.25},
        {"CampaignID": "CAMP005", "SpentAmount": 980.00},
    ]
    
    spent_amounts = [ad['SpentAmount'] for ad in simulated_data]
    
    if spent_amounts:
        total = sum(spent_amounts)
        average = total / len(spent_amounts)
        
        print("\n" + "=" * 70)
        print("RESULTS (Simulated Data)")
        print("=" * 70)
        print(f"Number of ads starting on {target_date_str}: {len(spent_amounts)}")
        print(f"Total spent: ${total:,.2f}")
        print(f"Average spent per ad: ${average:,.2f}")
        print("=" * 70)
        
        return average
    else:
        print("\nNo ads found for the target date.")
        return 0

if __name__ == "__main__":
    analyze_dorohedoro_ads()
