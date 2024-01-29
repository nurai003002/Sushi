from begin import rise
from vegatebles import vegetables_fish,collapse
from fish_sous import fish,sous,cut


def choice():
     while True:
          choice = input("хотите приготовить еще? 'да', 'нет': ")
          if choice == "нет":
               print(f'Мы приготовили  ваш заказ')
               break     
          elif choice == "да":
                    print(f"\n")
                    rise()
                    vegetables_fish()
                    collapse()
                    fish()
                    sous()
                    cut() 