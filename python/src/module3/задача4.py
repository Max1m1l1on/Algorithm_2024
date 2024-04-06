def z_function(string):
    Z = [0] * len(string)
    l = 0
    r = 0
    maximum_index = 0
    for i in range(1, len(string)):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < len(string) and string[Z[i]] == string[Z[i] + i]:
            Z[i] += 1

        if Z[i] > Z[maximum_index]:
            maximum_index = i

        if i + Z[i] - 1 > r:
            l = i
            r = i + Z[i] - 1

    return Z, maximum_index

def min_len(string):
    z, maximum_index = z_function(string)
    if maximum_index + z[maximum_index] == len(string):
        return len(string) - z[maximum_index]
    else:
        k = 0
        for i in range(len(string) - 1, -1, -1):
            if z[i] > k and z[i] < z[maximum_index] and i + z[i] == len(string):
                k = z[i]             

        return len(string) - k


if __name__ == "__main__":
    string = input()

    print(min_len(string))