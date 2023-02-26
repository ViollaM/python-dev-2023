import random
import argparse
import os.path
import urllib.request

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = 0
    guess_list = list(guess)
    secret_list = list(secret)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            bulls += 1
    
    cows = -bulls
    for i in range(len(guess_list)):
        if guess_list[i] in secret_list:
            cows += 1
            secret_list.remove(guess_list[i])
    
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    attempts = 0
    guess = ""

    while (guess != secret):
        guess = ask("Введите слово: ", words)
        attempts += 1
        bulls, cows = bullscows(guess, secret)
        inform("Быки {}, Коровы {}", bulls, cows)
    
    return attempts

def ask(prompt: str, valid: list[str] = None) -> str:
    print(prompt)
    word = input()
    if valid:
        while (not word in valid):
            print(prompt)
            word = input()
    return word

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog = 'BullsCows',
                        description = 'Bulls & Cows game')
    
    parser.add_argument("dictionary", action="store", type=str, help="Filename or URL where to get a dictionary of valid words")
    parser.add_argument("length", action="store", type=int, default=5, nargs="?", help="Length of words used in the game")

    args = parser.parse_args()

    dict = []
    if os.path.exists(args.dictionary):
        with open(args.dictionary, 'r') as f:
            for line in f.readlines():
                word = line.strip()
                if len(word) == args.length:
                    dict.append(word)
    else:
        with urllib.request.urlopen(args.dictionary) as f:
            for line in f.readlines():
                word = line.decode('utf-8').strip()
                if len(word) == args.length:
                    dict.append(word)

    if len(dict) == 0:
        print("Похоже в словаре нет слов заданной длины, попробуйте изменить длину или словарь")
    else:
        attempts_count = gameplay(ask, inform, dict)
        print(f"Поздравляем, вы угадали слово за {attempts_count} попыток!")
