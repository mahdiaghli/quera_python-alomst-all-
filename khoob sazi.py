import re


def words_check(text):
    words = text.split()
    words2 = []
    for word in words:
        word = word.lower()
        word = word[0].upper() + word[1:]

        myword = ""
        number = 0
        for char in word:
            if re.match(r"^[a-zA-Z]$", char):
                number = number + 1
                myword = myword + char

        if number > len(word) / 2:
            words2.append(myword)
    print(words2)

    dict = {}
    words2 = sorted(words2)
    for word in words2:
        dict[word] = words2.count(word)
    # dict = sorted(dict.keys())
    return dict


print(words_check("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
