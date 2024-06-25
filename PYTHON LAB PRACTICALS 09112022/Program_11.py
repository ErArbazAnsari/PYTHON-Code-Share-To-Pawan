print("***** WRITE A PYTHON FUNCTION THAT TAKES TWO LISTS AND RETURNS \nTRUE IF THEY ARE EQUAL OTHERWISE FALSE. *****")


def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

first_list = [10, 10, 11, 12, 12, 13, 14, 16, 15, 16, 12]
sec_list = [16, 12, 13, 14, 15, 16, 10, 11, 12, 10, 12]
if check_if_equal(first_list, sec_list):
    print('Lists are equal \ni.e. contain similar elements with same frequency')
else:
    print('Lists are not equal')