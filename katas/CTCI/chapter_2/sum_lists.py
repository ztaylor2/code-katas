"""Sum two linked lists."""

from kth_to_last import LinkedList


def sum_lists(list1, list2):
    """Sum two linked lists."""
    first_num = ''
    second_num = ''

    while list1.peek():
        first_num += str(list1.pop())

    while list2.peek():
        second_num += str(list2.pop())

    list_sum = str(int(first_num) + int(second_num))

    sum_list = LinkedList()

    for letter in list_sum:
        sum_list.push(int(letter))

    return sum_list
