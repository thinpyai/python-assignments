def validate(input : str):
    """
    Validate the valid bracket string.
    input : bracket string input.
    """

    expected_start = ['{','[', '(']
    expected_pair = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
    }

    input_char_list = list(input)
    expected_end = []

    if not input_char_list:
        return False
    
    if not input_char_list[0] in expected_start:
        return False

    for each_char in input_char_list:
        if expected_pair.get(each_char):
            expected_end.append(expected_pair.get(each_char))
        elif expected_end and expected_end[-1] == each_char:
            expected_end.pop()
        else:
            return False

    if expected_end:
        return False

    return True 
        


if __name__ == "__main__":
    sample_input_list = [
        '{}', # valid
        '{[', # invalid
        '{[}', # invalid
        '{[]}', # valid
        '' # Invalid
    ]

    for user_input in sample_input_list:

        if validate(user_input):
            print('Valid')
        else :
            print('Invalid')
