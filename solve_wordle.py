import random
#Made by Abraham Holleran

def get_dictionary(word_len):
  """
  word_len: the length of words that you want the resulting dictionary to be.
  This function opens the words_alpha file and returns only the words of length word_len
  with NO DUPLICATE LETTERS in the words.
  returns:: a list of all english words of length word_len
  """
  word_file = open("words_alpha.txt")
  words = word_file.readlines()
  word_file.close()
  no_duplicates = [i[:-1] for i in words if len(set(i[:-1])) == word_len & len(i[:-1]) == word_len]
  return no_duplicates


def common_letters(word_dictonary):
  """
  word_dictionary: The dictionary of words
  This function counts the occurances of each letter in the dictionary
  returns:: a dictionary object containing each letter paired with its number of occurances.
  """ 
  letters = {}
  for word in word_dictonary:
    for letter in word:
      if letter not in letters:
        letters[letter] = 0 #1 will be added soon
      letters[letter] += 1
  return letters 
  
def best_words(dictionary, letter_frequency, duplicates=False):
  letter_frequency
  """
  dictionary:: the dictionary to look through
  letter_frequency:: the number of occurances of each letter
  duplicates:: a bool that triggers duplicates in letters off
  This function finds the words in the dictionary that contain the most common letters.
  It evaluates each dictionary word by summing up the occurences for each letter.
  returns a list of tuples and the tuples are the weight with the word.
  """
  word_list = []
  for word in dictionary:
    word_set = word
    if not duplicates:
      word_set = set(word)
    weight = sum([letter_frequency[l] for l in word_set])
    word_list.append((weight, word))

  return sorted(word_list, reverse=True)

def wordle_filter_by_result(dict_word, guess_word, result_of_guess):
"""
Checks each word and sees if it could be correct
dict_word:: the word to Checks
guess_word:: the most recent guess that allows us to filter the dictionary
result_of_guess:: a key to help us see which letters of the guess are right.
for example: bwwbc
c means correct letter correct location, used when you guess the right letter in the final word.
w means correct letter wrong location, used when your word contains a letter in the final word.
b means wrong letter, used when a letter is not in the final answer
returns:: boolean for if the test passed or failed
"""
  for idx, letter in enumerate(result_of_guess):
    if letter == "c":
      if guess_word[idx] != dict_word[idx]:
        return False
    elif letter == "w":
      if (guess_word[idx] not in dict_word[:idx]+dict_word[idx+1:]):
        return False
    elif letter == "b":
      if guess_word[idx] in dict_word:
        return False
  return True

def wordle_filter_dict(recent_guess, guess_result, dicti):
  """
  This function goes through the list dictionary and only returns the elements that pass
  the filter test.
  returns:: a list
  """
  result = []
  for word in dicti:
    if wordle_filter_by_result(dict_word = word, guess_word = recent_guess, result_of_guess = guess_result):
      result.append(word)
  return result

def main(n):
  """
  This function solves the wordle game by giving you the best guesses at each moment.
  It filters the dictionary after each guess.
  n:: the number of letters you want to play with.
  """
  fivedict = get_dictionary(n)
  top_26_dict = common_letters(fivedict)
  guess = best_words(fivedict, top_26_dict)[0][1]
  print(f"Your first guess should be {guess}.")
  for i in range(10):
    recent_result = input("What was your result? c,w,b: ")
    for i in recent_result:
      assert i in ["c","w","b"]
    fivedict = wordle_filter_dict(recent_guess = guess, guess_result = recent_result, dicti = fivedict)
    top_26_dict = common_letters(fivedict)
    guess = best_words(fivedict, top_26_dict)[0][1]
    print(f"Your guess is {guess}.")

    
print("Welcome to a solver for Wordle! Just enter the result of your guess and the solver will print out your best option for a guess. In this version of Wordle, letters aren't duplicated. So, \"snooks\" wouldn't be allowed. Also, format the result of your guess by typing a c for a correct letter guessed, w for a letter in the wrong spot, and b for a letter that's not in the correct wordle. For example, you might enter \"bbcwwbb\". Enjoy!")
n = int(input("How many letters (1-15) would you like to play with? "))
if n < 1 or n > 15:
  print("Your number is not in the range 1-15.")
main(n)
