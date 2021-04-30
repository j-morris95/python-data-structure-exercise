def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    sorted_list1 = list(str(num1))
    sorted_list1.sort()
    sorted_list2 = list(str(num2))
    sorted_list2.sort()
    return "".join(sorted_list1) == "".join(sorted_list2)
