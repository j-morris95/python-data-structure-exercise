def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_dict = {}
    for ltr in phrase:
        letter_dict[ltr] = letter_dict.get(ltr, 0) + 1
    return letter_dict

   # I solved using this line below which I think is a better solution, but
   # test 1 fails because the set reorders 'yay' to {'a', 'y'}
   # however the returned dictionary still accurately counts the
   # number of occurrences of each letter in the phrase
   ###
   # return {ltr: phrase.count(ltr) for ltr in set(phrase)}
