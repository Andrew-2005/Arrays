# Знаходить вершину після строгого підйому й перевіряє строгий спуск.
def validMountainArray(arr) -> bool:
    last = len(arr) - 1
    if last < 2:
        return False

    index = 0
    while index < last and arr[index] < arr[index + 1]:
        index += 1
    if index == 0 or index == last:
        return False

    while index < last and arr[index] > arr[index + 1]:
        index += 1
    return index == last


if __name__ == "__main__":
    assert validMountainArray([2, 1]) is False
    assert validMountainArray([3, 5, 5]) is False
    assert validMountainArray([0, 3, 2, 1]) is True
    assert validMountainArray([0, 1, 2, 3, 4, 2, 1]) is True
    assert validMountainArray([0, 2, 3, 3, 5, 2, 1]) is False
    assert validMountainArray([]) is False
    assert validMountainArray([1, 2, 3]) is False
    assert validMountainArray([3, 2, 1]) is False
    assert validMountainArray([-3, -1, -2]) is True
    print("OK")
