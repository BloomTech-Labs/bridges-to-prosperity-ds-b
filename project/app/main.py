from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import get_data

app = FastAPI(
    title="Labs28 Bridges to Prosperity TeamB DS Backend",
    description="Returns relevant bridge data as list of JSON",
    version="0.4",
    docs_url="/",
)

# app.include_router(predict.router)
# app.include_router(viz.router)
# app.include_router(raw.router)
# app.include_router(sites.router)
# app.include_router(villages.router)
# app.include_router(final_data.router)
app.include_router(get_data.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app)
