# from fastapi import FastAPI
# from src.config.settings import settings
# from src.common.database import init_engine

from src.squads.e3_2_marketplace.routes import router as marketplace_router
# from src.common.logger import setup_logging

# setup_logging()

# app = FastAPI(title="Admin Dashboard - Marketplace Oversight (E3.2)")

# # initialize DB engine (creates engine based on settings)
# init_engine(settings.DATABASE_URL)

# # include routers
# app.include_router(marketplace_router, prefix="/api/v1/admin/marketplace", tags=["marketplace"])

# @app.get("/")
# def health():
#     return {"status": "ok", "service": "admin-dashboard-service", "squad": "E3.2"}




# from fastapi import FastAPI
# from src.common.database import engine, Base
# from src.squads.e3_3_services import routes as services_routes
# from src.common.logger import logger

# # create DB tables (for dev small demo). For production use alembic migrations.
# def create_tables():
#     Base.metadata.create_all(bind=engine)

# def build_app():
#     app = FastAPI(title="Admin Dashboard Service - E3.3 Services Oversight")
#     app.include_router(services_routes.router)
#     return app

# app = build_app()

# @app.on_event("startup")
# def on_startup():
#     logger.info("Starting app... creating tables (dev mode)")
#     create_tables()



from fastapi import FastAPI
from src.common.database import engine, Base
from src.squads.e3_3_services import routes as services_routes
from src.common.logger import logger


def create_tables():
    Base.metadata.create_all(bind=engine)


def build_app():
    app = FastAPI(title="Admin Dashboard Service - E3.3 Services Oversight")
    app.include_router(marketplace_router, prefix="/api/v1/admin/marketplace", tags=["marketplace"])
    app.include_router(services_routes.router)
    return app


app = build_app()


@app.on_event("startup")
def on_startup():
    logger.info("Starting app... creating tables (dev mode)")
    create_tables()
