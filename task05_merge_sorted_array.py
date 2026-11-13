# Заповнює nums1 з кінця, щоразу вибираючи найбільший із решти елементів.
def merge(nums1, m, nums2, n) -> None:
    first, second = m - 1, n - 1
    write = m + n - 1

    while second >= 0:
        if first >= 0 and nums1[first] > nums2[second]:
            nums1[write] = nums1[first]
            first -= 1
        else:
            nums1[write] = nums2[second]
            second -= 1
        write -= 1


if __name__ == "__main__":
    for nums1, m, nums2, n, expected in (
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([], 0, [], 0, []),
        ([-3, 0, 0, 0], 2, [-4, 0], 2, [-4, -3, 0, 0]),
        ([4, 5, 0, 0], 2, [1, 2], 2, [1, 2, 4, 5]),
    ):
        assert merge(nums1, m, nums2, n) is None
        assert nums1 == expected
    print("OK")
