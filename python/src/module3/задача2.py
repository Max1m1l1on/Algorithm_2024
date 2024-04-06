def get_hash(stroka_t, len_stroka):
    p = 10**9 + 7
    x = 31
    stroka_hash = 0
    for i in range(len_stroka):
        stroka_hash = (stroka_hash * x + ord(stroka_t[i])) % p
    return stroka_hash

def cyclic_shift(stroka_t, stroka_s):
    p = 10**9 + 7
    x = 31
    string_hash = get_hash(stroka_t, len(stroka_s))
    substring_hash = get_hash(stroka_s, len(stroka_s))
    sliding_hash = 1
    for i in range(len(stroka_s)):
        sliding_hash = (sliding_hash * x) % p


    for i in range(len(stroka_t) - len(stroka_s) + 1):
        if substring_hash == string_hash:
            return i
        if i + len(stroka_s) < len(stroka_t):
            string_hash = (string_hash * x - ord(stroka_t[i]) * sliding_hash + ord(stroka_t[i + len(stroka_s)])) % p
            string_hash = (string_hash + p) % p
    return -1

if __name__ == "__main__":
    stroka_s = input()
    stroka_t = input()
    stroka_t = stroka_t * 2
    p = 10**9 + 7
    x = 31
    print(cyclic_shift(stroka_t, stroka_s))