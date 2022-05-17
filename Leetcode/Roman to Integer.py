def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    # Store the result
    result = 0
    # Use to judge jump or not
    flag_jump = False
    # A dictionary to store the value
    dict_sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(s)):
        # Code for jump to the next iteration
        if flag_jump == True:
            flag_jump = False
            continue
        # If next character is bigger than current character, combine them together and add the value
        if i + 1 < len(s):
            if dict_sym[s[i + 1]] > dict_sym[s[i]]:
                flag_jump = True
                result += (dict_sym[s[i + 1]] - dict_sym[s[i]])
                continue

        result += dict_sym[s[i]]

    return result


print(romanToInt('IV'))