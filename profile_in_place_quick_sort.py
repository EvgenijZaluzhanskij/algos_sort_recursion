@profile
def partition(nums, left, right):
    if left > right:
        return

    pivot_index = left + (right - left) // 2
    pivot = nums[pivot_index]

    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1

        while left <= right and nums[right] > pivot:
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        else:
            break

    return left, right


@profile
def in_place_quick_sort(input_array, start, end):
    if end < start:
        return

    p = partition(input_array, start, end)
    in_place_quick_sort(input_array, start, p[1])
    in_place_quick_sort(input_array, p[0], end)


def main():
    input_data = [5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10,
                  11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5,
                  14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12,
                  3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7,
                  2, 5, 14, 15, 5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15]
    # input_data = [1, 2, 3, 4, 5]

    in_place_quick_sort(input_data, 0, len(input_data) - 1)

    print(input_data)


if __name__ == '__main__':
    main()
