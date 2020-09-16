from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

sites_ids = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/feature/final-data-output/data/edit/B2P_Rwanda_Sites%2BIDs_full_2020-09-16.csv"
sites_ids = pd.read_csv(sites_ids)

# reordering 'sites_ids' to desired output format
"""
# Desired Output Format
const bridgeSite = {
  id: 1014107,
  name: "Buzi",
  type: "Suspended",
  stage: "Rejected",
  subStage: "Technical",
  individualsDirectlyServed: 0.0,
  span: "",
  latitude: -2.42056,
  longitude: 28.9662,
  communitiesServed: [
    {
      id: 22050101,
      name: "Agahehe",
    },
    {
      id: 22050102,
      name: "Kabacuzi",
    },
    {
      id: 22050103,
      name: "Kamutozo",
    },
    {
      id: 22050104,
      name: "Kamweko",
    },
  ],
};
"""

column_order = [
    "Project Code",
    "Bridge Site Name",
    "Bridge Type",
    "Project Stage",
    "Project Sub-Stage",
    "Individuals Directly Served",
    "Span (m)",
    "GPS (Latitude)",
    "GPS (Longitude)",
    "Communities_Served",
]

sites_ids = sites_ids.reindex(columns=column_order)

# /final-data endpoint
@router.get("/final-data")
async def final_data():
    output = sites_ids.to_json(orient="records")
    parsed = json.loads(output)
    return parsed
