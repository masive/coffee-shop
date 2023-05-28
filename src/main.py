from fastapi import FastAPI
from routers import index

app = FastAPI(title="coffee-shop", docs_url="/swagger")
app.include_router(index.router, prefix="", tags=["ping"])
