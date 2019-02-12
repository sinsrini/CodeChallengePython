'''
Write a function that accepts an integer and returns True if the input is between 4 and 10, inclusive; otherwise, return False
'''

def test_a(n):
    '''
    :param number: Integer value
    :return: True if number is between  4 and 10, False otherwise
    '''
    if n >=4 and n <= 10:
        return True
    else:
        return False

print test_a(4)


'''
Write a function to test if a list contains any items. Return 'EMPTY' if it does not contain any items and 'NOT EMPTY' if it does.
'''

def test_b(list):
    '''

    :param list: List of any length
    :return:
    '''
    if len(list)==0:
        return "EMPTY"
    else:
        return "NON EMPTY"

print test_b([])

'''
Write a function that accepts a file name and a string and writes the string to the file with the given file name.
'''

def test_c(f_name, text):
    '''

    :param f_name: <filename>
    :return:
    '''
    f = open(f_name,"a")
    f.write(text)
    f.close()

test_c("test1.txt", "Append this text")

'''
Write a function that accepts a list and doubles each value in the list. When no input parameter is provided, return an empty list.
'''
def test_d(list = None):
    '''

    :param list: A list
    :return: list with values doubled
    '''
    if list is not None:
        return map(lambda i: i+i, list)
    else:
        return []

print test_d([2,6,8])