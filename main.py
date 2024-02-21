def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    num_words = word_count(text)
    letter_dict = count_letters(text)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    sort_on(letter_dict)
    print("--- End report ---")    

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(file_contents):
    words = len(str(file_contents).split())
    return words
    
def count_letters(text):
    letter_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
    return letter_dict    

def sort_on(dict):
  key_list = []
  for key in dict:
    key_list.append(key)
  sorted_list = sorted(key_list)
  

  for element in sorted_list:
    print(f"The {element} character was found {dict[element]} times")

main()