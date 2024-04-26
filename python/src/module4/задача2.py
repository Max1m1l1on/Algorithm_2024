def sort_of_wagon(list_of_wagons):
    stack = list()
    check_number = 1
    for i in list_of_wagons:
        while len(stack) > 0 and stack[-1] == check_number:
            stack.pop()
            check_number = check_number + 1
        if i == check_number:
            check_number = check_number + 1
        else:
            stack.append(i)
    
    while len(stack) > 0:
        if stack.pop() != check_number:
            return "NO"
        check_number = check_number + 1
    return "YES" 
        
if __name__ == "__main__":
    number = int(input())
    list_of_wagons =  list(map(int, input().split()))
    print(sort_of_wagon(list_of_wagons))
    