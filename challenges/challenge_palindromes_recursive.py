def is_palindrome_recursive(word, low_index, high_index):
    if not word or word == '':
        return False
    if word[low_index] != word[high_index]:
        return False

    if high_index <= low_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


teste = is_palindrome_recursive("daad", 0, -1)
print(teste)
