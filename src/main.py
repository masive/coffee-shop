from fastapi import FastAPI
from routers import api

app = FastAPI(title="coffee-shop", docs_url="/swagger")
app.include_router(api.router)
