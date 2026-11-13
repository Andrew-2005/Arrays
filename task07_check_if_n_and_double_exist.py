# Шукає подвоєне значення або цілу половину серед уже переглянутих чисел.
def checkIfExist(arr) -> bool:
    seen = set()
    for value in arr:
        if 2 * value in seen or (value % 2 == 0 and value // 2 in seen):
            return True
        seen.add(value)
    return False


if __name__ == "__main__":
    assert checkIfExist([10, 2, 5, 3]) is True
    assert checkIfExist([3, 1, 7, 11]) is False
    assert checkIfExist([0, 0]) is True
    assert checkIfExist([0, 1]) is False
    assert checkIfExist([0]) is False
    assert checkIfExist([-3, -6]) is True
    assert checkIfExist([-6, -3]) is True
    assert checkIfExist([-3, -2]) is False
    print("OK")
