import random
import os


def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return(words)


def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data)
    chosen_word_trans = chosen_word.maketrans('áéíóú', 'aeiou')
    chosen_word_unaccented = chosen_word.translate(chosen_word_trans)
    chosen_word_list = [letter for letter in chosen_word_unaccented]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word_unaccented):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    lives = 7
    
    while True:
        os.system("cls")
        print("¡Adivina la palabra!")
        print("Tienes: ", lives, " vidas")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            lives -= 1

        if lives == 0:
            print("Has perdido, inténtalo de nuevo :(, la palabra era: ", chosen_word)
            break
        
        if "_" not in chosen_word_list_underscores:
            os.system("cls")
            print("¡Ganaste! La palabra era", chosen_word)
            break


if __name__ == '__main__':
    run()