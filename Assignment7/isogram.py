def is_isogram(xword):
    d = {}
    for i in xword:
        if not i in d.keys():
            d[i] = 1
        else:
            d[i] += 1
            if d[i] > 1:
                return False
    return True


if __name__ == "__main__":
    words = ["dermatoglyphics", "palindrome", "anagram"]

    for w in words:
        print(is_isogram(w))