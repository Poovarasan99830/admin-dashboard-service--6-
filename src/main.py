from fastapi import FastAPI
from src.config.settings import settings
from src.common.database import init_engine, get_engine, Base

# Import routers
from src.squads.e3_1_user_mgmt import routes as user_routes
# from src.squads.e3_2_marketplace.routes import router as marketplace_router
# from src.squads.e3_3_services import routes as services_routes
# from src.squads.e3_4_payments import routes as payments_routes
# from src.squads.e3_5_analytics import routes as analytics_router

app = FastAPI(title="Admin Dashboard Service", version="0.1.0")

# Init DB
init_engine(settings.DATABASE_URL)

@app.on_event("startup")
def on_startup():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)

# Routers
app.include_router(user_routes.router, prefix="/api/v1/admin/users", tags=["users"])
# app.include_router(marketplace_router, prefix="/api/v1/admin/marketplace", tags=["marketplace"])
# app.include_router(services_routes.router, prefix="/api/v1/admin/services", tags=["services"])
# app.include_router(payments_routes.router, prefix="/api/v1/admin/payments", tags=["payments"])
# app.include_router(analytics_router, prefix="/api/v1/admin/analytics", tags=["analytics"])

@app.get("/")
def health():
    return {"status": "ok"}
