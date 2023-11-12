def decrypt(original, key):
    result = ""

    for char in key:
        if char in original:
            index = original.find(char)
            original = original[:index] + original[index + 1:]

    result = original

    return result