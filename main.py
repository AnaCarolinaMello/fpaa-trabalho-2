def max_min_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    
    if right - left == 1:
        if arr[left] > arr[right]:
            return arr[left], arr[right]
        return arr[right], arr[left]

    mid = (left + right) // 2
    
    max1, min1 = max_min_select(arr, left, mid)
    max2, min2 = max_min_select(arr, mid + 1, right)
    
    return max(max1, max2), min(min1, min2)

def find_max_min(arr):
    if not arr:
        return None, None
    return max_min_select(arr, 0, len(arr) - 1)


print("Encontrar o máximo e o mínimo de um array")

number = 0
arr = []

while (number != "r"):
    print("Digite um número ou r para ver o resultado")
    number = input()
    try:
        arr.append(float(number))
    except ValueError:
        if number != "r":
            print("Número inválido")

max_val, min_val = find_max_min(arr)
print(f"Máximo: {max_val}, Mínimo: {min_val}")
