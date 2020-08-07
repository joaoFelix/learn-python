# Prints all inputs, with first letter capitalized, until input = '\end'
# A '.' is added to sentences and a '?' to questions

# 1: if input == '\end':
#   1.1: print all previous inputs
#   1.2: end (break while)
# 2: if input != '\end':
#   2.1: check if input is question
#       2.1.1: return True if first word in a list of "question starter words" or False otherwise
#   2.2: Add a "?" to input if is question or a "." otherwise
#   2.3: Store input in a list
#   2.4: continue asking for input


# assume no abbreviations like "How's" instead of "How is"
def is_question(phrase):
    question_starters = ('how', 'why', 'what')
    return phrase.startswith(question_starters)  # Tests if a string starts with any of the tuple items


def add_punctuation(phrase):
    if is_question(phrase):
        return "{}?".format(phrase)

    return "{}.".format(phrase)


def format_phrase(phrase):
    return phrase.capitalize()


def build_output(phrases):
    separator = ' '
    return separator.join(phrases)


all_inputs = []

while True:
    user_input = input('Say something: ')
    if user_input == '\\end':
        break
    else:
        user_input = add_punctuation(user_input)
        user_input = format_phrase(user_input)
        all_inputs.append(user_input)

print(build_output(all_inputs))
