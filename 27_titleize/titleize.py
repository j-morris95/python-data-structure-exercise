def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_arr = phrase.lower().split(" ")
    char_arr = [[char for char in word] for word in word_arr]
    for i in range(len(char_arr)):
        char_arr[i][0] = char_arr[i][0].upper()

    return " ".join(["".join(char_list) for char_list in char_arr])

    # didn't know about title and capitalize methods.... but this works I guess
