# Збирає парні й непарні числа в окремі групи та з’єднує їх.
def sortArrayByParity(nums) -> list:
    even, odd = [], []
    for value in nums:
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    return even + odd


if __name__ == "__main__":
    for nums in ([3, 1, 2, 4], [0], [], [1, 3, 1], [2, 0, 2], [-3, -2, 0, 3, -2]):
        original = sorted(nums)
        even_count = sum(value % 2 == 0 for value in nums)
        result = sortArrayByParity(nums)
        assert sorted(result) == original
        assert all(value % 2 == 0 for value in result[:even_count])
        assert all(value % 2 == 1 for value in result[even_count:])
    print("OK")
