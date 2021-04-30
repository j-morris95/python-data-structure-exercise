def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    low = phrase.lower()
    return {char: low.count(char) for char in set(low) if char in 'aeiou'}

    # this solution is more efficient, but doesn't return the exact same order
    # key value pairs are the same but the test result is also comparing
    # order of the dictionary which I disagree since a dictionary is meant
    # to be used to look things up and order doesn't matter
