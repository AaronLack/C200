def palindrome(x):
    word = ""
    for i in x:
        word = i + word
    if word == x:
        return True
    else:
        return False

        
print(palindrome("aba"))                        #True
print(palindrome("a"))                          #True
print(palindrome("abba"))                       #True
print(palindrome("amanaplanacanalpanama"))      #True
print(palindrome("abca"))                       #False
print(palindrome("ac"))                         #False
print(palindrome("adabbba"))                    #False
print(palindrome("amandaplanacanalpanama"))     #False


if __name__== "main":
    pass