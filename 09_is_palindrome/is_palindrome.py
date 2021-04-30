def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    orig_phrase = phrase.replace(' ', '').upper()
    phrase_list = [c.upper() for c in phrase.replace(' ', '')]
    phrase_list.reverse()
    reversed_phrase = "".join(phrase_list)
    if (orig_phrase == reversed_phrase):
        return True
    return False
