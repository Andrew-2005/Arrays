# Рухаючись справа наліво, записує поточний максимум праворуч.
def replaceElements(arr) -> list:
    if not arr:
        return arr

    greatest = arr[-1]
    arr[-1] = -1
    for index in range(len(arr) - 2, -1, -1):
        value = arr[index]
        arr[index] = greatest
        greatest = max(greatest, value)
    return arr


if __name__ == "__main__":
    assert replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert replaceElements([400]) == [-1]
    assert replaceElements([]) == []
    assert replaceElements([3, 3, 3]) == [3, 3, -1]
    assert replaceElements([-2, -4, -8]) == [-4, -8, -1]
    print("OK")
