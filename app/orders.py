from fastapi import APIRouter

router = APIRouter()

orders = {}  

@router.post("/order")
def place_order(order: dict):
    order_id = len(orders) + 1
    orders[order_id] = order
    return {"message": "Zamówienie przyjęte"}

@router.get("/orders")
def get_orders():
    return orders