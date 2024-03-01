def merge_sort(s):
    if len(s) > 1:
        mid = len(s) // 2
        left_half = s[:mid]
        right_half = s[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(s, left_half, right_half)


def merge(merged, left_half, right_half):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left_half) and right_cursor < len(right_half):
        if left_half[left_cursor] <= right_half[right_cursor]:
            merged[left_cursor + right_cursor] = left_half[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right_half[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left_half)):
        merged[left_cursor + right_cursor] = left_half[left_cursor]

    for right_cursor in range(right_cursor, len(right_half)):
        merged[left_cursor + right_cursor] = right_half[right_cursor]

    return merged


def sort_string(string):
    sorted_string = list(string.lower())
    merge_sort(sorted_string)
    return "".join(sorted_string)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        sorted_first = sort_string(first_string)
        sorted_second = sort_string(second_string)
        return (sorted_first, sorted_second, False)

    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    return (sorted_first, sorted_second, sorted_first == sorted_second)
