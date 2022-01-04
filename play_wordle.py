import random

def get_dictionary(word_len):
  word_file = open("words_alpha.txt")
  words = word_file.readlines()
  word_file.close()
  no_duplicates = [i[:-1] for i in words if len(set(i[:-1])) == word_len & len(i[:-1]) == word_len]
  return no_duplicates

def play_wordle(n):
  word_dictionary = get_dictionary(n)
  WORD = random.choice(word_dictionary)
  for i in range(10):
    correctly_formated_answer = False
    while not correctly_formated_answer:
      guess = input(f"{i}/10. Enter your guess: ")
      if len(guess) != n:
        print(f"Your word isn't of length {n}. Please try again.")
      elif guess in word_dictionary:
        correctly_formated_answer = True
      elif len(set(guess)) < len(guess):
        print(f"Your guess, \"{guess}\", contains duplicate letters. Please try again with a word without duplicates.")
      else:
        print(f"Your guess, \"{guess}\", is not in our dictionary. Please try again.")
    to_print = ""
    for idx, letter in enumerate(guess):
      if guess[idx] == WORD[idx]:
        to_print += "c"
      elif guess[idx] in WORD:
        to_print += "w"
      else:
        to_print += "b"
    if "b" not in to_print and "w" not in to_print:
      print("You won!")
    else:
      print(to_print)

n = int(input("How many letters would you like to play with? "))
play_wordle(n)
