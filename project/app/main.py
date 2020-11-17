from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import get_data

app = FastAPI(
    title="Labs28 Bridges to Prosperity TeamB DS Backend",
    description=f"Returns relevant bridge data in JSON.",
    version="0.5",
    docs_url="/",
)

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
