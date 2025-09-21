from fastapi import FastAPI
from src.config.settings import settings
from src.common.database import init_engine

from src.squads.e3_2_marketplace.routes import router as marketplace_router
from src.common.logger import setup_logging

setup_logging()

app = FastAPI(title="Admin Dashboard - Marketplace Oversight (E3.2)")

# initialize DB engine (creates engine based on settings)
init_engine(settings.DATABASE_URL)

# include routers
app.include_router(marketplace_router, prefix="/api/v1/admin/marketplace", tags=["marketplace"])

@app.get("/")
def health():
    return {"status": "ok", "service": "admin-dashboard-service", "squad": "E3.2"}
