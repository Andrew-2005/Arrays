# Рахує числа з парною кількістю цифр у записі без знака.
def findNumbers(nums) -> int:
    return sum(len(str(abs(value))) % 2 == 0 for value in nums)


if __name__ == "__main__":
    assert findNumbers([12, 345, 2, 6, 7896]) == 2
    assert findNumbers([555, 901, 482, 1771]) == 1
    assert findNumbers([]) == 0
    assert findNumbers([0, 9, 10, 99, 100, 1000]) == 3
    assert findNumbers([-9, -10, -1000]) == 2
    print("OK")
