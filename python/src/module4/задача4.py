def minimums(numbers, step):
    deque = list()
    answer = list()
    for i in range(len(numbers)):
        while (len(deque) > 0) and (deque[0] < (i - step + 1)):
            deque.pop(0)
        while (len(deque) > 0) and (numbers[deque[-1]] > numbers[i]):
            deque.pop()
        deque.append(i)
        if i >= step - 1:
            answer.append(numbers[deque[0]])
    return answer

if __name__ == "__main__":
    number, step = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = minimums(numbers, step)
    for i in answer:
        print(i)