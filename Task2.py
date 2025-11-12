def min_steps_to_equal(arr, k):
    n = len(arr)
    
    if len(set(arr)) == 1:
        return 0 
    
    if len(set(arr)) == n:
        return -1
        
    if k <= 0 or k > n:
        return -1
    
    from collections import Counter
    counter = Counter(arr)
    target = counter.most_common(1)[0][0]
    
    positions = [i for i, x in enumerate(arr) if x == target]
    
    min_steps = float('inf')
    
    for pos in positions:
        steps = 0
        current_pos = pos
        
        for i in range(n):
            if arr[i] != target:
                if current_pos < i:
                    distance = i - current_pos
                else:
                    distance = n - current_pos + i
                    
                steps_for_this = (distance + k - 2) // (k - 1)
                steps = max(steps, steps_for_this)
        
        min_steps = min(min_steps, steps)
    
    return min_steps if min_steps != float('inf') else -1

def main():
    while True:
        try:
            input_str = input("Введите элементы массива через пробел: ")
            arr = list(map(int, input_str.split()))
            if not arr:
                print("Массив не может быть пустым!")
                continue
            break
        except ValueError:
            print("Пожалуйста, вводите только целые числа, разделенные пробелами!")
    
    n = len(arr)
    
    while True:
        try:
            k = int(input("Введите число K: "))
            if k <= 0:
                print("K должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    
    result = min_steps_to_equal(arr, k)
    
    if result == 0:
        print("0")
    elif result == -1:
        print("-1")
    else:
        print(f"{result}")
    
if __name__ == "__main__":
    main()
