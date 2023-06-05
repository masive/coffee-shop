from fastapi import FastAPI
from routers import health, customer

app = FastAPI(title="coffee-shop", docs_url="/swagger")
app.include_router(health.router, tags=["health"], prefix="/api/v1")
app.include_router(customer.router, tags=["customers"], prefix="/api/v1")
