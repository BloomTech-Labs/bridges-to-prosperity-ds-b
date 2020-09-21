from fastapi import APIRouter
import pandas as pd
import json
import csv
import io
import requests

router = APIRouter()


# /final-data endpoint
@router.get("/final-data")
async def final_data():
    # output = sites_ids.to_json(orient="records")
    # parsed = json.loads(output)
    # return parsed
    """
    Desired Format
{
  project_code: 1014107,
  district: "whatever",
  province: "province",
  sector: "sector",
  cell: "cell",
  village: "village",
  village_id: 342343,
  name: "Buzi",
  type: "Suspended",
  stage: "Rejected",
  sub_stage: "Technical",
  individuals_directly_served: 0.0,
  span: "",
  lat: -2.42056,
  long: 28.9662,
  communities_served: [
      "Agahehe",
      "Kabacuzi",
      "Kamutozo",
      "Kamweko",
  ],
};
    """

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
            communities_served = "NO COMMUNITIES SERVED"
        else:
            communities_served = list(row["communities_served"].split(", "))

        # Set key for dictionary
        key = row["project_code"]

        # Set output format
        output[key] = {
            "project_code": row["project_code"],
            "province": row["province"],
            "district": row["district"],
            "sector": row["sector"],
            "cell": row["cell"],
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
        }

    # Return output
    return output
