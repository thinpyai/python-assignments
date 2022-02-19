def order(sentence: str) -> str:
    """Order the string

    is2 Thi1s T4est 3a  -->  Thi1s is2 3a T4est
    4of Fo1r pe6ople g3ood th5e the2  -->  Fo1r the2 g3ood 4of th5e pe6ople

    Args:
        sentence (_type_): Reordered sentence
    """  
    words = sentence.split(' ')
    reorder_sentence = ''
    
    numbers_words_pairs = []
    for word in words:
        pair = {int(char): word for char in word if char.isdigit()}
        keys = list(pair.keys())

        # e.g. p1e6ople => consider as 16
        if len(keys) > 1:
            str_keys = [ str(key) for key in keys]
            key_str = ''.join(str_keys)
            pair = {int(key_str): pair[keys[0]]}
        numbers_words_pairs.append(pair)

    for i in range(len(numbers_words_pairs)):
        current_pair = numbers_words_pairs[i]

        if not current_pair:
            continue

        current_num = list(current_pair.keys())[0] 
        for j in range(i+1, len(numbers_words_pairs)):
            next_pair = numbers_words_pairs[j]
            next_num = list(next_pair.keys())[0]
            if current_num > next_num:
                temp_pair = numbers_words_pairs[i]
                numbers_words_pairs[i] = next_pair
                numbers_words_pairs[j] = temp_pair
                current_pair = numbers_words_pairs[i]
                current_num = list(current_pair.keys())[0] 

    for pair in numbers_words_pairs:
        if reorder_sentence:
            reorder_sentence += ' '
        if not pair:
            continue
        reorder_sentence += list(pair.values())[0]

    return reorder_sentence

# OK answer
# Not working : to solve
def order2(sentence: str):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# OK answer
def order3(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

if __name__ == "__main__":
    print(order3('is2 Thi1s T4est 3a'))
    # order('4of Fo1r pe6ople g3ood th5e the2')
    # order('')