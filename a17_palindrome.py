# Palindrome

# def palindrome():
#     x = input("Enter word or phrase to test: ")
#     x = x.lower()
#     if x == x[::-1]:
#         print("It is palindrome.")
#     else:
#         print("It is not palindrome.")
# palindrome()


def palindrome():
    x = input("Enter word or phrase to test: ")
    x = x.lower()
    return x == x[::-1]

print(palindrome())