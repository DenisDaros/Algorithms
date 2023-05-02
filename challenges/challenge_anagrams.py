def selection_sort(string):
    array = list(string.lower())
    n = len(array)
    for i in range(n):
        min_element_index = i
        for j in range(i+1, n):
            if array[j] < array[min_element_index]:
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]
    return ''.join(array)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)

    sorted_first = selection_sort(first_string)
    sorted_second = selection_sort(second_string)

    boolean = sorted_first == sorted_second

    return (
        sorted_first,
        sorted_second,
        boolean
    )
