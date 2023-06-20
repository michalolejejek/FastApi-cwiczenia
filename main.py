from fastapi import FastAPI
from app.menu import router as menu_router
from app.orders import router as orders_router

app = FastAPI()

app.include_router(menu_router, prefix="/api")
app.include_router(orders_router, prefix="/api")