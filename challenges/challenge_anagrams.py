def merge_sort(s):
    if len(s) > 1:
        mid = len(s) // 2
        left_half = s[:mid]
        right_half = s[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(s, left_half, right_half)


def merge(s, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            s[k] = left_half[i]
            i += 1
        else:
            s[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        s[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        s[k] = right_half[j]
        j += 1
        k += 1


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
