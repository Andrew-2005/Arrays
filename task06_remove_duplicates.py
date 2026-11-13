# Записує кожне нове значення в наступну позицію унікального префікса.
def removeDuplicates(nums) -> int:
    k = 0
    for value in nums:
        if k == 0 or value != nums[k - 1]:
            nums[k] = value
            k += 1
    return k


if __name__ == "__main__":
    for nums, expected in (
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([], []),
        ([7, 7, 7], [7]),
        ([-3, -1, 0, 4], [-3, -1, 0, 4]),
    ):
        k = removeDuplicates(nums)
        assert k == len(expected)
        assert nums[:k] == expected
    print("OK")
