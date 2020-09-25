from fastapi import APIRouter
import pandas as pd
import json
import csv
import io
import requests

router = APIRouter()


# /final-data/extended endpoint
@router.get("/final-data/extended")
async def final_data_extended():

    # Loading data from URL
    request = requests.get(
        "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/main/data/edit/B2P_Rwanda_Sites%2BIDs_full_2020-09-21.csv"
    )
    buff = io.StringIO(request.text)
    directread = csv.DictReader(buff)

    output = {}

    # Loop over rows and return according to desired format
    for row in directread:

        # splitting "communities_served" into list of strings with every
        # iteration
        if len(row["communities_served"]) == 0:
            communities_served = ["unavailable"]
        else:
            communities_served = list(row["communities_served"].split(", "))

        # Set key for dictionary
        key = row["project_code"]

        # Set output format
        output[key] = {
            "project_code": row["project_code"],
            "province": row["province"],
            "district": row["district"],
            "district_id": row["district_id"],
            "sector": row["sector"],
            "sector_id": row["sector_id"],
            "cell": row["cell"],
            "cell_id": row["cell_id"],
            "village": row["village"],
            "village_id": row["village_id"],
            "name": row["name"],
            "type": row["type"],
            "stage": row["stage"],
            "sub_stage": row["sub_stage"],
            "Individuals_directly_served": int(row["Individuals_directly_served"]),
            "span": int(row["span"]),
            "lat": float(row["lat"]),
            "long": float(row["long"]),
            "communities_served": communities_served,
            "form": row["form"],
            "case_safe_id": row["case_safe_id"],
            "opportunity_id": row["opportunity_id"],
            "country": row["country"],
            }

    # Return output
    return output
