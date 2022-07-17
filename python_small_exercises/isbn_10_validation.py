from multiprocessing.sharedctypes import Value


def valid_ISBN10(isbn: str) -> bool: 

    val_list = [char for char in isbn]

    if len(val_list) != 10:
        return False

    val = 0

    for index in range(1,11):
        try:
            val += calculate_each(index, val_list[index-1])
        except ValueError:
            return False
    
    if val % 11 == 0:
        return True

    return False

def calculate_each(index: int, input: str):
    if index == 10 and input == 'X':
        input = '10'
    
    input_int = int(input)

    return index * input_int

def good_ans(isbn):
    return bool(re.match("\d{9}[\dX]$", isbn)) and sum("0123456789X".index(d) * i for i, d in enumerate(isbn, 1)) % 11 == 0
    
if __name__ == "__main__":
    # print(valid_ISBN10('1112223339'))
    print(valid_ISBN10('X123456788'))