def easy_quick_sort(input_array):
    if input_array:
        left_result = easy_quick_sort(
            [e for e in input_array[1:] if e < input_array[0]]
        )

        right_result = easy_quick_sort(
            [e for e in input_array[1:] if e >= input_array[0]]
        )

        return left_result + input_array[0:1] + right_result

    return []


if __name__ == '__main__':
    input_data = [5, 4, 12, 3, 10, 11, 12, 7, 2, 5, 14, 15]

    print(easy_quick_sort(input_data))
