def has_negatives(a):
    cache = {}
    positives = []
    result = []
    for i in a:
        if i > 0:
            positives.append(i)
        else:
            cache[i + (i * -2)] = i
    for i in positives:
        if i in cache:
            result.append(i)


    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
