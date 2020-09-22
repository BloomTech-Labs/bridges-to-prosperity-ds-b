from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, raw, sites, villages, final_data, final_data_extended

app = FastAPI(
    title="Labs25-Bridges_to_Prosperity-TeamB-ds",
    description="Replace this placeholder text",
    version="0.3",
    docs_url="/",
)

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(raw.router)
app.include_router(sites.router)
app.include_router(villages.router)
app.include_router(final_data.router)
app.include_router(final_data_extended.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app)
