import json


def remove_repeat_char(f_str, second_str):
    # print(str)
    first_characters = list(f_str)
    second_characters = second_str.split()

    print(first_characters)
    repeats = []
    for i in range(len(first_characters)):
        if first_characters[i] == first_characters[i-1]:
            if first_characters[i] not in repeats:
                repeats.append(first_characters[i])
        else:
            repeats.append(first_characters[i])

    print("-------------------", repeats)


def kalameh(str):
    foshs = open("./fosh.json", encoding="utf8")
    foshs = json.load(foshs)["word"]
    # print(foshs)

    words = str.split()

    for i in range(len(words)):
        # if word in foshs:
        #     print(word)

        # Punctuation marks
        # word_with_punctuation = word.split("،")
        # if len(word_with_punctuation) == 2:
        #     if word_with_punctuation[0] in foshs:
        #         print("found punctuation marks", word_with_punctuation[0])
        #     if word_with_punctuation[1] in foshs:
        #         print("found punctuation marks", word_with_punctuation[1])

        next_word = words[i + 1] if i + 1 < len(words) else ""
        remove_repeat_char(words[i], next_word)


strK = "سلام و کیر خر، کیررر خررر کیییرررر خر و خروار ،خر قرم ساق"
kalameh(strK)
