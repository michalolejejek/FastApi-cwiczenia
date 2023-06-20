from fastapi import APIRouter

router = APIRouter()

orders = []  #lista slownikow

@router.post("/order")
def place_order(order: dict):
    orders.append(order)
    return {"message": "Zamówienie przyjęte"}

@router.get("/orders")
def get_orders():
    return orders

#kazde zamowienie to slownik z menu ktore przekazywane jest ze wszystkimi indentyfikatorami.
