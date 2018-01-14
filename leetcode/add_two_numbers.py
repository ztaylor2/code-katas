"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


def add_two_numbers(ll1, ll2):
    """."""
    num1 = ''
    node1 = ll1.head
    while node1:
        num1 = node1.val + num1
        node1 = node1.next
    num1 = int(num1)

    num2 = ''
    node2 = ll2.head
    while node2:
        num2 = node2.val + num2
        node2 = node2.next
    num2 = int(num2)

    sum = str(num1 + num2)

    sum_list = LinkedList()

    for num in sum:
        sum_list.push(num)

    return sum_list
