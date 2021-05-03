def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    counter = 0
    if len(parens) % 2 == 1:
        return False
    for paren in parens:
        if paren == "(":
            counter += 1
        elif paren == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0
