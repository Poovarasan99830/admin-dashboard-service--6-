# Admin Dashboard - Marketplace Oversight (E3.2)

Run locally:
1. create .env with DATABASE_URL
2. pip install -r requirements.txt
3. python scripts/seed_db.py
4. uvicorn src.main:app --reload

APIs:
- GET /api/v1/admin/marketplace/flagged
- POST /api/v1/admin/marketplace/flagged/{id}/resolve
- POST /api/v1/admin/marketplace/disputes/{id}/resolve

Note: use header `x-api-key` with ADMIN_API_KEY value from .env to pass RBAC check.
