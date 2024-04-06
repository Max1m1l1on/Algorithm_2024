def prefix_function(stroka):
    res = [0] * len(stroka)
    res[0] = 0
    for i in range(len(stroka) - 1):
        j = res[i]
        while (j > 0) and (stroka[i + 1] != stroka[j]):
            j = res[j - 1]
        if stroka[i + 1] == stroka[j]:
            res[i + 1] = j + 1
        else:
            res[i + 1] = 0
    return res

def repeated_string(stroka):
    prefix = prefix_function(stroka)
    n = len(stroka) - prefix[-1]
    if len(stroka) % n == 0:
        return n
    return len(stroka)


if __name__ == "__main__":
    stroka = input()
    strochka = repeated_string(stroka)
    print(len(stroka) // strochka)
    