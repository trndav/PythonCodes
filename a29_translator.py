# Translator

words = {"ball": "lopta", "rain": "kisa", "sand": "pijesak", "is": "je", "round": "okrugla"}

def translator():
    usr = input("Type words to transalte:\n").split()
    for word in usr:
        if word in words:
            print(words[word], end=" ")
        else:
            print(f"{word} is not in dictionary.")

translator()


# words = {"ball": "lopta", "rain": "kisa", "sand": "pijesak", "is": "je", "round": "okrugla"}
# def translator():
#     usr = input("Type words to translate:\n").split()
#     translated = []
#     for word in usr:
#         if word in words:
#             translated.append(words[word])
#         else:
#             translated.append(f"({word} not found)")
#     print(" ".join(translated))
# translator()