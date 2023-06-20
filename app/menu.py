from fastapi import APIRouter

router = APIRouter()

menu = {}  # Słownik na potrawy w menu

@router.post("/menu")
def add_dish(dish: dict):
    dish_id = len(menu) + 1
    menu[dish_id] = dish
    return {"message": "Potrawa dodana do menu"}

@router.get("/menu")
def get_menu():
    return menu