# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word = input('Enter a word: ')
    anagram = input('Enter second word: ')

    sorted_str1 = sorted(word)
    sorted_str2 = sorted(anagram)

    if (sorted_str1 == sorted_str2):
     return True
    else:
     
     return False
find_anagram("word","anagram")
