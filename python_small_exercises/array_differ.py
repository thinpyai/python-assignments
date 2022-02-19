def array_diff(a: list = [], b: list = []) -> list:
    """
    Diff two arrays by removing same iteams of b from a

    Args:
        a (list, optional): List of items. Defaults to [].
        b (list, optional): List of items_. Defaults to [].

    Returns:
        list: Remaing items in a after removing same items from b.
    """    
    a = [] if not a else a
    b = [] if not b else set(b)

    c = [val for val in a if val not in b]
    return c

if __name__ == "__main__":
    print(array_diff([1], None))