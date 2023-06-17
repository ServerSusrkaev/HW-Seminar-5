def degree(x, y):
    result = x ** y
    return result

def recursive_sum(x, y):
    if x == 0:
        return y
    else:
        return recursive_sum(x - 1, y + 1)