import random
import re 

words = ['apple', 'banana', 'mango', 'pear', 'orange', 'kiwi', 'pineapple' , 'apricot' ,'lemon', 'coconut', 'watermelon' ,
'cherry' ,'papaya', 'berry' ,'peach' ,'lychee' ,'muskmelon']



def print_word(word):
    for char  in word:
        print(f' {char} ', end='')



while True:
    random_word = random.choice(words)
    telling  = print(f'Ми звгвдали вам слово.\nЦе якийсь фрукт. у вас є {len(random_word)+2}  спроб щоб відгадати\nЯкщо ви не вгадаєте 2 рази гра закінчиться')
    
    chance = len(random_word) +2
    guessed_word = ["_"] * len(random_word)
    print_word(guessed_word)
    no_ges  = 0
    is_alphabet = re.compile(r'^[a-zA-Z]$')
    try:
        while (True) and chance != 0:
            ask_letter = input(' введіть букву: ')
            if is_alphabet.match(ask_letter):
                pass
            else:
                print('введіть будь ласка одну  букву на англ! ')
                continue
            if ask_letter in random_word:
                for index, word in enumerate(random_word):
                    if word == ask_letter:
                        guessed_word[index] = ask_letter
                    else:
                        pass
            else:
                no_ges += 1
                chance -= 1
                if no_ges >= 3:
                        print('YOU LOSEEER AHAHAH')
                        print(f' it was {random_word}')
                        break
                pass

            print(f'у вас лишилось {chance} спроб')
            print_word(guessed_word)
            if "_" not in guessed_word:
                print(" You win! ")
                break
            if chance == 0:
                print('YOU LOSEEER AHAHAH')
                print(f' it was {random_word}')
                break

    except ValueError:
        print("Цієї букви не має в слові :(")


    play_again = input('Бажаєте спробувати ще раз? (так/ні): ')
    
    if play_again.lower() != 'так':
        break





