# Переносить елементи з кінця й записує тільки ті позиції, які вміщаються.
def duplicateZeros(arr) -> None:
    size = len(arr)
    write = size + arr.count(0) - 1
    for read in range(size - 1, -1, -1):
        value = arr[read]
        if write < size:
            arr[write] = value
        write -= 1

        if value == 0:
            if write < size:
                arr[write] = 0
            write -= 1


if __name__ == "__main__":
    for arr, expected in (
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([0], [0]),
        ([0, 0, 0], [0, 0, 0]),
        ([0, 1, 0, 2], [0, 0, 1, 0]),
        ([1, 2, 0], [1, 2, 0]),
    ):
        assert duplicateZeros(arr) is None
        assert arr == expected
    print("OK")
