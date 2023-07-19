import re


def is_valid(c):
    return re.match('[\w ]', c) is not None


def has_spam(s):
    return len(re.findall('spam', s.lower())) != 0


name = input()
content = input()

number = 0
for char in content:
    if is_valid(char) is False:
        number = number + 1

# print(name.isdigit())
# print(has_spam(content))
# print(number)
# print(len(content))
# if number >= len(content):
#     print("are")

if (has_spam(content) is False or number < len(content) / 2) and name.isdigit() is False:
    print("Not Spam")

if (has_spam(content) is True and number >= len(content) / 2) and name.isdigit() is False:
    print("Invalid Content")

if (has_spam(content) is False or number < len(content) / 2) and name.isdigit() is True:
    print("Invalid Sender")

if (has_spam(content) is True and number >= len(content) / 2) and name.isdigit() is True:
    print("Fully Invalid")
