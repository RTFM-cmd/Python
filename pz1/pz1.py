# Игра "Угадайка"
import random

def main():
    
    number = random.randint(0, 100)
    while True:
        answer = input('Угадайте число: ')
        if answer == 'exit':
            break

        if answer.isdigit() == False:
            print('Вы ввели нечисловое значение, попробуйте еще раз')
            continue
        answer = int(answer)
    
        if answer == number:
            print('Успех')
            break
        
        elif answer < number:
            print('Бери выше')
        else:
            print('Бери ниже')
