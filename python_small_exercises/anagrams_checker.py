# What is an anagram? Well, two words are anagrams of each other 
# if they both contain the same letters. For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

from collections import defaultdict

def anagrams(word, words):
    key_chars = get_char_count(word)
    
    results = []
    for w in words:
        search_chars = get_char_count(w)
        if key_chars == search_chars:
            results.append(w)
    
    return results

def get_char_count(word):
    chars = defaultdict(int)
    for char in word:
        chars[char] += 1
    return chars 

def anagrams_2(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]

def anagrams_3(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)

from collections import Counter

def anagrams_4(word, words):
    counts = Counter(word)
    return [w for w in words if Counter(w) == counts]

if __name__ == "__main__":
    print(anagrams('abab',['aabb','abcd','bbaa','aaab']))
    
