#Sorting
def bubble_sort(items, key_function, ascending=True):
    """
    Sort a list using Bubble Sort.

    items:
        The list to be sorted.

    key_function:
        A function that tells the sorter what value to compare.

    ascending:
        True  = ascending order
        False = descending order
    """

    sorted_list = items.copy()
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            current_value = key_function(sorted_list[j])
            next_value = key_function(sorted_list[j + 1])

            if ascending:
                if current_value > next_value:
                    sorted_list[j], sorted_list[j + 1] = (
                        sorted_list[j + 1],
                        sorted_list[j]
                    )
            else:
                if current_value < next_value:
                    sorted_list[j], sorted_list[j + 1] = (
                        sorted_list[j + 1],
                        sorted_list[j]
                    )

    return sorted_list