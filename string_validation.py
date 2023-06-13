import re

regex1 = "(a+b) (a+b)* (aa+bb) (ab+ba) (a+b)* (aba+baa)"
pattern1 = r"^[ab](?:[ab])*(?:aa|bb)(?:ab|ba)(?:[ab])*?(?:aba|baa)$"

regex2 = "(11+00) (1+0)* (101+111+01) (00*+11*) (1+0+11)"
pattern2 = r"^(?:11|00)(?:1|0)*(?:101|111|01)(?:00*|11*)(?:1|0|11)$"

# str = input("Input a string: ")

def validateString(pattern, string):
    if re.match(pattern, string):
        print("Match found!")
        validate = "Valid String"
    else:
        print("No match.")
        validate = "Invalid String"
    return validate


# validateString(pattern2, str)

# continuee = input("Continue? Y/N: ")

# while True:
#     if (continuee == 'Y'):
#         str = input("Input a string: ")
#         validateString(pattern2, str)
#         continuee = input("Continue? Y/N: ")
#     else:
#         break
