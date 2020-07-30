def convert_emojis(msg):
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }

    words = msg.split(" ")  # words is a list

    output = emojis.get(words[0], words[0])

    for word in words[1:]:
        output += " " + emojis.get(word, word)

    return output


message = input("> ")

print(convert_emojis(message))

