from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

names_codes = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/main/data/edit/Rwanda_Administrative_Levels_and_Codes_Province_through_Village_clean_2020-08-25.csv"
names_codes = pd.read_csv(names_codes)

# /villages endpoint
@router.get("/villages")
async def villages():
    output = names_codes.to_json(orient="records")
    parsed = json.loads(output)
    return parsed
