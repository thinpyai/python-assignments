def rgb(r: int, g: int, b: int):
    """
    The rgb function is incomplete. Complete it so that passing in RGB decimal values 
    will result in a hexadecimal representation being returned. Valid decimal values 
    for RGB are 0 - 255. Any values that fall out of that range must be rounded to 
    the closest valid value.

    Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

    The following are examples of expected output values:

    Args:
        r (int): Red
        g (int): Green
        b (int): Blue
    """     
    return get_hex_str(r)+get_hex_str(g)+get_hex_str(b)

def get_hex_str(val: int) -> str:
    """
    Get hexadecimal string from integer value

    Args:
        val (int): Value

    Returns:
        str: hexadecimal string
    """    
    target_val = min([val, 255]) if val > 0 else 0
    val_str = f'{target_val:02X}'
    return val_str

def rgb_2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

def rgb_3(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))

if __name__ == "__main__":
    print(rgb(255, 255, 255) ) # returns FFFFFF
    print(rgb(255, 255, 300) ) # returns FFFFFF
    print(rgb(0,0,0) ) # returns 000000
    print(rgb(148, 0, 211) ) # returns 9400D3
