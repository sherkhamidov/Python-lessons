#  SOZ TOPISH OYINI
# import random
# from uzwords import words

# def get_words():
#     word = random.choice(words)
#     while "-" in word or  ' ' in word:
#         word = random.choice(words)
#     return word.upper()

# def display( user_letters, words):
#     display_letters=""
#     for letter in word:
#         if letter in user_letters.upper():
#             display_letter += letter
#         else:
#             display_letter +="-"
#     return display_letter

#     def play():
#         word = get_word()
#         word_letters = set(word)

#         user_letters = ' '
#         print(f"men {len [word]} xonali so'z o'yladim. topa olaszmi")
#         print(word)
#         while len(word_letters)>0:
#             print(display(user_letters, words))  
#             if len(user_letters)>0:
#                 print('shu vaqtgacha kiritgan harflaringiz {user_letters}')

#             letter = input("harf_kiriting").upper() 
#             if letter in user_letters:
#                 print("bu harfni avval kiritgansz iltmos boshqa kirirting")
#                 continue
#             elif letter in words:
#                 word_letters.remove(letters)
#                 print(f"{letter} harfi tog'ri")
#             else:
#                 print(f"bunday harf yoq.")
#             user_letters += letter
#         print(f"tabriklayman! {word} so'zini {len(user_letters)} ta urunishda topdingiz.")

