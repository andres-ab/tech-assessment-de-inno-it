import pandas as pd
import json

def convert_to_json(df):
    
    # Drop columns that contain only NaN values
    df = df.dropna(axis=1, how='all')

    # Initialize the dictionary to store the final JSON
    json_data = {}

    # Create a dictionary to store data for each Market
    markets_data = {}

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        # Get values from columns
        schema_version = row['schemaVersion']
        extract_start_datetime = row['extractStartDateTime']
        market_iso_code = row['Market_isoCode']
        market_store_id = row['Market_storeId']
        interval_start = row['Interval_start']
        interval_end = row['Interval_end']
        average_ticket_currency = row['AverageTicket_currency']

        # Check if the column contains "_"
        for col in df.columns:
            if '_' in col:
                keys = col.split('_')
                if not pd.isnull(row[col]):
                    # Check if all values in the column are NaN
                    if keys[-1] == "isoCode" or keys[-1] == "storeId":
                        markets_data[index, keys[-1]] = row[col]
                    elif keys[-1] == "start" or keys[-1] == "end":
                        markets_data[index, keys[-1]] = row[col]
                    elif keys[-1] == "tier" or keys[-1] == "amount":
                        markets_data[index, keys[-1]] = row[col]
            else:
                json_data[col] = row[col]

        # Build the JSON structure for each Market
        market_dict = {
            "isoCode": markets_data.get((index, "isoCode"), ""),
            "storeId": int(markets_data.get((index, "storeId"), 0))
        }
        interval_dict = {
            "start": markets_data.get((index, "start"), ""),
            "end": markets_data.get((index, "end"), "")
        }
        tier_dict = {
            "tier": markets_data.get((index, "tier"), 0),
            "amount": markets_data.get((index, "amount"), 0)
        }

        # Add to the final JSON
        if "MarketsList" not in json_data:
            json_data["MarketsList"] = []

        # Check if the current Market is already in the list
        market_exists = any(market["Market"] == market_dict for market in json_data["MarketsList"])

        if not market_exists:
            json_data["MarketsList"].append({
                "Market": market_dict,
                "Interval": interval_dict,
                "AverageTicket": {
                    "currency": average_ticket_currency,
                    "TiersList": [tier_dict]
                }
            })
        else:
            # If the Market already exists, append only the Tier to the existing Market
            existing_market = next(market for market in json_data["MarketsList"] if market["Market"] == market_dict)
            existing_market["AverageTicket"]["TiersList"].append(tier_dict)

    # Convert the dictionary to JSON format
    json_result = json.dumps(json_data, indent=2)

    return json_result
