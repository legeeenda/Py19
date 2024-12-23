from task1.models import Buyer, Game


def run():
    if not Buyer.objects.exists():  # Если покупателей еще нет
        buyer1 = Buyer.objects.create(name="JohnDoe", balance=100.00, age=25)
        buyer2 = Buyer.objects.create(name="JaneDoe", balance=150.00, age=17)
        buyer3 = Buyer.objects.create(name="Alice", balance=200.00, age=30)

        game1 = Game.objects.create(title="Adventure Quest", cost=50.00, size=5.5, description="An amazing RPG game.", age_limited=False)
        game2 = Game.objects.create(title="War Zone", cost=60.00, size=10.0, description="A thrilling FPS game.", age_limited=True)
        game3 = Game.objects.create(title="Puzzle Master", cost=40.00, size=3.0, description="A challenging puzzle game.", age_limited=True)

        game1.buyer.set([buyer1])
        game2.buyer.set([buyer1])
        game3.buyer.set([buyer1])

        game1.buyer.add(buyer2)
        game2.buyer.add(buyer3)
        game3.buyer.add(buyer3)
        print("База данных успешно заполнена.")
    else:
        print("База данных уже заполнена, пропускаем.")
