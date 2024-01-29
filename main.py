from hay import registration
from begin import rise
from begin import rise
from vegatebles import vegetables_fish,collapse
from  fish_sous import fish,sous,cut
from end import choice



user = input("У вас есть свой кабинет:  'да', 'нет': ")
if user == 'да':
    rise()
elif user == 'нет':
    registration()
else:
    print('Ошибка введите данные варианты')
        
rise()
vegetables_fish()
collapse()
fish()
sous()
cut() 
choice()
    