
def vegetables_fish():
    print("Есть 5 видов оващей ")
    print("огурцом","помидором","авокадой","морковкой","капустой")
    vegetables =input("Выбериты оващ: ")

    vegetables_1 ="огурцом"
    vegetables_2 ="помидором"
    vegetables_3 ="авокадой"
    vegetables_4 ="морковкой"
    vegetables_5 ="капустой"

    if vegetables == "огурцом":
        print(f"рис с '{vegetables_1}' готова, тепер добавте рыбу")
    elif vegetables == "помидором":
        print(f"рис с '{vegetables_2}' готова, тепер добавте рыбу")
    elif vegetables == "авокадой":
        print(f"рис с '{vegetables_3}' готова, тепер добавте рыбу")
    elif vegetables == "морковкой":
        print(f"рис с '{vegetables_4}' готова, тепер добавте рыбу")
    elif vegetables == "капустой":
        print(f"рис с '{vegetables_5}' готова, тепер добавте рыбу")

    print("Есть 3 видов рыб")
    print("угорь", "лосось", "окунь")
    fish = input("Выберите рыбу: ")

    fish_1 = "угорём"
    fish_2 = "лососям"
    fish_3 = "окунем"

    if fish == "угорь":
        print(f"рис с '{vegetables}' и {fish_1} готова")
    elif fish == "лосось":
        print(f"рис с '{vegetables}' и {fish_2} готова")
    elif fish == "окунь":
        print(f"рис с '{vegetables}' и {fish_3} готова")

def collapse():
    user = input("Введите слово (свернули) чтобы свернут суши: ")
    if user == "свернули":
        print(f"вы {user} суши ")
        