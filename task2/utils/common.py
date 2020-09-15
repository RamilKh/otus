from task2.configs.const import SPEED_DIRECTORY_PLURAL


# get plural word by number
def plural(number, words):
    if number % 10 == 1 and number % 100 != 11:
        result = words[0]
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        result = words[1]
    else:
        result = words[2]

    return result


# get plural for speed
def plural_speed(number, label):
    words = (number, number, number)
    values = SPEED_DIRECTORY_PLURAL

    if values.get(label.name) is not None:
        words = values[label.name]

    return plural(number, words)
