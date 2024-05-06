# code by X
# Return a sequence of numbers counting by `x` `n` times.
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(i * x)
    return result
