# Підраховує поточну серію одиниць і запам’ятовує найдовшу.
def findMaxConsecutiveOnes(nums) -> int:
    longest = current = 0
    for value in nums:
        if value == 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


if __name__ == "__main__":
    assert findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
    assert findMaxConsecutiveOnes([]) == 0
    assert findMaxConsecutiveOnes([0, 0]) == 0
    assert findMaxConsecutiveOnes([1, 1, 1]) == 3
    print("OK")
