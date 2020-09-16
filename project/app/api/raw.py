from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

site_assessment = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/main/data/raw/B2P_Rwanda_Site_Assessment_Data.csv"
site_assessment = pd.read_csv(site_assessment)


@router.get("/raw")
async def raw():
    output = site_assessment.to_json(orient="records")
    parsed = json.loads(output)
    return parsed
