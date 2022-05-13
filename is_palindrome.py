def is_palindrome(s):
    if s == "" or s is None:
        return False
    string = ''
    for character in s:
        if character.isalnum():
            string += character

    string = string.lower()
    ans = (string == string[::-1])

    return ans
