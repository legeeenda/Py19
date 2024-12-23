from task1.models import Buyer, Game
from django.contrib.auth.hashers import make_password
def run():
    print("Запуск функции populate_db...")

    buyers_exist = Buyer.objects.exists()
    games_exist = Game.objects.exists()

    if not buyers_exist or not games_exist:
        print("Создаем покупателей и игры...")


        buyer1, _ = Buyer.objects.get_or_create(
            name="JohnDoe", 
            defaults={"balance": 100.00, "age": 25, "password": make_password("password123")}
        )
        buyer2, _ = Buyer.objects.get_or_create(
            name="JaneDoe", 
            defaults={"balance": 150.00, "age": 17, "password": make_password("password456")}
        )
        buyer3, _ = Buyer.objects.get_or_create(
            name="Alice", 
            defaults={"balance": 200.00, "age": 30, "password": make_password("password789")}
        )
        buyer4, _ = Buyer.objects.get_or_create(
            name="555", 
            defaults={"balance": 200.00, "age": 30, "password": make_password("password789")}
        )


        game1, _ = Game.objects.get_or_create(
            title="Adventure Quest",
            defaults={"cost": 50.00, "size": 5.5, "description": "An amazing RPG game.", "age_limited": False}
        )
        game2, _ = Game.objects.get_or_create(
            title="War Zone",
            defaults={"cost": 60.00, "size": 10.0, "description": "A thrilling FPS game.", "age_limited": True}
        )
        game3, _ = Game.objects.get_or_create(
            title="Puzzle Master",
            defaults={"cost": 40.00, "size": 3.0, "description": "A challenging puzzle game.", "age_limited": True}
        )

        game1.buyer.set([buyer1])  
        game2.buyer.set([buyer1])  
        game3.buyer.set([buyer1])
        game3.buyer.set([buyer1])


        game1.buyer.add(buyer2)  
        game2.buyer.add(buyer3)  
        game3.buyer.add(buyer3) 
        game3.buyer.add(buyer4)


        print("Игры успешно связаны с покупателями.")
    else:
        print("База данных уже заполнена, пропускаем.")


def fix_default_passwords():

    buyers = Buyer.objects.filter(password="default_password")
    for buyer in buyers:

        buyer.password = make_password("new_secure_password")
        buyer.save()
    print(f"Обновлено {buyers.count()} записей.")
