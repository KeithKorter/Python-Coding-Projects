def first_4(item):
    return item[:4]
def first_and_last_4(item):
    return item[:4] + item[-4::1]
def odds(item):
    return item[1::2]
def reverse_evens(item):
    temp = item[::2]
    return temp[::-1]