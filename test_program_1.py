'''
Given the below function, please describe test scenarios for the below function.
NOTE: When describing your scenarios, it's OK to use simple scenario descriptions for your tests.

'''

def format_zipcode(zip_code):
    if len(zip_code) <= 5:
        return '{:>05}'.format(zip_code)
    if len(zip_code) == 10:
        return str(zip_code)
    if len(zip_code) == 9:
        return '{}-{}'.format(zip_code[:5], zip_code[5:])

'''
Test Scenarios:
1. Input zipcode of length 5, assert it returns the zipcode as it is.
2. Input zipcodes of length less than 5:
    a. for zipcode with length 4, assert it returns the zipcode with 0 inserted at the beginning (to make it right aligned to 5 positions)
    b. for zipcode with length 3, assert it retruns the zipcode with 00 inserted at the beginning
3. Input zipcodes of length greater than 5 but less than 9, assert it returns None.
4. Input zipcode of length 9, assert it returns zipcode which is split as <first five numbers> - <last four numbers>.
5. Input zipcode of length 10, assert it returns zipcode in string format.
6. Input zipcode of length 11, assert it returns None.
7. Input zipcodes of length greater than 10 say 20 or 50, assert it returns None.
8. Input empty zipcode, assert it returns 00000. (5 zeros so as to align to 5 positions)
9. Call function without any input, it should throw as error.
'''