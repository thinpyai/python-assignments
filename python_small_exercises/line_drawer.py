def draw_square(size: int):
    """
    Draw square
    e.g.
    +----------+
    |          |
    |          |
    |          |
    |          |
    |          |
    +----------+

    Args:
        size (int): size of object
    """    
    print('+'+ size * '-' +'+')
    print(('|'+ size * ' ' +'|\n') * (size//2), end='')
    print('+'+ size * '-' +'+')

if __name__ == "__main__":
    draw_square(10)