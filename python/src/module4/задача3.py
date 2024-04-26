def nearest_smaller_one(numbers):
    stack = list()
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while len(stack) > 0 and numbers[stack[-1]] > numbers[i]:
            answer[stack.pop()] = i
        stack.append(i)
    return answer

if __name__ == "__main__":
    number = int(input())
    numbers = list(map(int, input().split()))
    answer = nearest_smaller_one(numbers)
    print(*answer)