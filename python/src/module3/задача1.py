def get_hash(stroka, len_stroka):
    p = 10**9 + 7
    x = 31
    stroka_hash = 0
    for i in range(len_stroka):
        stroka_hash = (stroka_hash * x + ord(stroka[i])) % p
    return stroka_hash

def the_Rabin_Karp_algorithm(stroka, strochka):
    p = 10**9 + 7
    x = 31
    stroka_hash = get_hash(stroka, len(strochka))
    substring_hash = get_hash(strochka, len(strochka))
    sliding_hash = 1
    for i in range(len(strochka)):
        sliding_hash = (sliding_hash * x) % p

    list_s_indexami = []

    for i in range(len(stroka) - len(strochka) + 1):
        if substring_hash == stroka_hash:
            list_s_indexami.append(i)
        if i + len(strochka) < len(stroka):
            stroka_hash = (stroka_hash * x - ord(stroka[i]) * sliding_hash + ord(stroka[i + len(strochka)])) % p
            stroka_hash = (stroka_hash + p) % p
    return list_s_indexami

if __name__ == "__main__":
    p = 10**9 + 7
    x = 31
    stroka = input()
    strochka = input()
    res = the_Rabin_Karp_algorithm(stroka, strochka)
    print(*res)