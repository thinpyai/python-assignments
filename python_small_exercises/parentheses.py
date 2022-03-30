def valid_parentheses(string):
    # takes a string of parentheses, and determines 
    # if the order of the parentheses is valid. 
    # The function should return true if the string is valid, 
    # and false if it's invalid.
    # "()"              =>  true
    # ")(()))"          =>  false
    # "("               =>  false
    # "(())((()())())"  =>  true

    # reg start count
    # reg stop reduce count 
    # when count negative False
    # open_count = len(re.findall(r'\(', string))
    # close_count = len(re.findall(r'\)', string))

    # if open_count != close_count:
    #     return False
    
    val = 0
    for c in string:
        val += 1 if c == '(' else  -1 if c == ')' else 0
        if val < 0: 
            return False
    
    if val != 0:
        return False

    return True


if __name__ == "__main__":
    print(valid_parentheses('(()')) # False