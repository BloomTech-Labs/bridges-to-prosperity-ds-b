from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

site_assessment = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/feature/DS-endpoints-sites-villages/data/edit/B2P_Rwanda_Site_Assessment_Data_clean_2020-08-25.csv"
site_assessment = pd.read_csv(site_assessment)

# /sites endpoint
@router.get("/sites")
async def sites():
    output = site_assessment.to_json(orient="index")
    parsed = json.loads(output)
    return parsed
