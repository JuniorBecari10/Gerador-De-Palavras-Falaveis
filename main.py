import random

consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vocals = ["a", "e", "i", "o","u"]

print("Gerador de Palavras Faláveis")
print("")

num_str = input("Digite o número de letras que essa palavra tenha: ")
num_int = int(num_str)

word = ""
time_consonant = True

for i in range(num_int):
    index = random.randint(0, len(consonants) if time_consonant else len(vocals)) - 1
    
    word += consonants[index] if time_consonant else vocals[index]
    
    time_consonant = not time_consonant

word = word.title()

print()
print("Palavra gerada:")
print(word)
