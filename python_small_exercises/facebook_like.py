# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. We want to 
# create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names 
# of people that like an item. It must return the display text as 
# shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names: list = []):

    list_len = len(names)
    end_word = ' like this' if list_len > 1 else ' likes this'

    if list_len > 3:
        start_word = f'{names[0]}, {names[1]} and {list_len-2} others'
    elif list_len == 3:
        start_word = f'{names[0]}, {names[1]} and {names[2]}'
    elif list_len == 2:
        start_word = f'{names[0]} and {names[1]}'
    elif list_len == 1:
        start_word = f'{names[0]}'
    else:
        start_word = 'no one'

    return start_word + end_word
  
def likes_best_answer(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

if __name__ == "__main__":
    likes_best_answer(['Jacob', 'Alex'])