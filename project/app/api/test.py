from fastapi import APIRouter, Body
import pandas as pd
import json
from itertools import chain
import csv
import io
import requests
from pydantic import BaseModel
import ast
from typing import List, Optional

router = APIRouter()

sites_ids = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/main/data/edit/B2P_Rwanda_Sites%2BIDs_full_2020-09-16.csv"
sites_ids = pd.read_csv(sites_ids)


# Renaming Column
sites_ids = sites_ids.rename(
    columns={
        "Project Code": "project_code",
        "Bridge Site Name": "name",
        "Village_ID": "village_id",
        "Village": "village",
        "Cell_ID": "cell_id",
        "Cell": "cell",
        "Sector_ID": "sector_id",
        "Sector": "sector",
        "Dist_ID": "district_id",
        "District": "district",
        "Province": "province",
        "Bridge Type": "type",
        "Project Stage": "stage",
        "Project Sub-Stage": "sub_stage",
        "Individuals Directly Served": "Individuals_directly_served",
        "Span (m)": "span",
        "GPS (Latitude)": "lat",
        "GPS (Longitude)": "long",
        "Communities_Served": "communities_served",
        "Form: Form Name": "form",
        "CaseSafeID Form": "case_safe_id",
        "Bridge Opportunity: Opportunity ID": "opportunity_id",
        "Country": "country",
        "Community Served 1": "community_served_1",
        "Community Served 2": "community_served_2",
        "Community Served 3": "community_served_3",
        "Community Served 4": "community_served_4",
        "Community Served 5": "community_served_5",
    }
)

# Dropping communities_served
sites_ids.drop("communities_served", 1, inplace=True)

# Adding new communties_served column
sites_ids["communities_served"] = (
    sites_ids["community_served_1"]
    + ", "
    + sites_ids["community_served_2"]
    + ", "
    + sites_ids["community_served_3"]
    + ", "
    + sites_ids["community_served_4"]
    + ", "
    + sites_ids["community_served_5"]
)


# Cleaning communities served
sites_ids["communities_served"].replace(r"\d+ and", "", regex=True, inplace=True)
sites_ids["communities_served"] = (
    sites_ids["communities_served"].str.lstrip("?,").str.strip(" ?,").str.rstrip(" ?")
)


# Column order
column_order = [
    "project_code",
    "province",
    "district",
    "district_id",
    "sector",
    "sector_id",
    "cell",
    "cell_id",
    "village",
    "village_id",
    "name",
    "type",
    "stage",
    "sub_stage",
    "Individuals_directly_served",
    "span",
    "lat",
    "long",
    "communities_served",
    "form",
    "case_safe_id",
    "opportunity_id",
    "country",
]

sites_ids = sites_ids.reindex(columns=column_order)

#####################################################


# /final-data endpoint
@router.get("/test")
async def test():
    data = {}
    r = requests.get(
        "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/feature/edit-final-output/data/edit/B2P_Rwanda_Sites%2BIDs_full_2020-09-21.csv"
    )
    buff = io.StringIO(r.text)
    dr = csv.DictReader(buff)
    for row in dr:
        # print(row)
        key = row["village_id"]
        data[key] = row
        cs = list(row["communities_served"].split(", "))
        return {"project_code": row["project_code"], "cs": cs}
