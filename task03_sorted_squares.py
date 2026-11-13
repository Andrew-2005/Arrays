# Заповнює результат із кінця, щоразу беручи більший квадрат із двох країв.
def sortedSquares(nums) -> list:
    squares = [0] * len(nums)
    left, right = 0, len(nums) - 1

    for index in range(right, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            squares[index] = nums[left] ** 2
            left += 1
        else:
            squares[index] = nums[right] ** 2
            right -= 1

    return squares


if __name__ == "__main__":
    assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sortedSquares([]) == []
    assert sortedSquares([-5, -3, -3, -1]) == [1, 9, 9, 25]
    assert sortedSquares([-2, 0, 0, 2]) == [0, 0, 4, 4]
    print("OK")
