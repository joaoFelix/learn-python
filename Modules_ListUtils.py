def find_max(number_list):
    maximum = number_list[0]

    for num in number_list[1:]:
        if num > maximum:
            maximum = num

    return maximum
