from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

sites_ids = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/feature/final-data-output/data/edit/B2P_Rwanda_Sites%2BIDs_full_2020-09-16.csv"
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
    }
)


# Reordering 'sites_ids' to desired output format + extension
"""
# Desired Output Format
const bridgeSite = {
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

# /final-data/extended endpoint
@router.get("/final-data/extended")
async def final_data_extended():
    output = sites_ids.to_json(orient="records")
    parsed = json.loads(output)
    return parsed
