def get_nth_value(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, values in enumerate(dictionary.values()):
        if i == n:
            return values
    raise IndexError("dictionary index out of range")