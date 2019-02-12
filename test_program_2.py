'''
Write a function that accepts two arbitrary strings and returns a new string containing only the unique characters present in both inputs.
Input:
The function must accept two string parameters.
Output:
The function must return a string.
'''

'''
As I was little confused with the meaning of "containing only the unique characters", I have written different functions for each case!

'''
def test_unique_characters(text_1, text_2):
    unique = ""
    if text_1 == text_2:
        return ""
    else:
        for i in text_1:
            if (i not in text_2) and (i not in unique):
                unique = unique + i
        for i in text_2:
            if i not in text_1 and i not in unique:
                unique = unique + i
    return unique

print test_unique_characters("python", "code")

# -----------------------------------------------------------------
# one more logic to test_unique_characters
def test_diff_characters(text1, text2):
    common1 = set(text1).difference(text2)
    common2 = set(text2).difference(text1)
    return ''.join(common1)+''.join(common2)

print test_diff_characters("python", "code")

# ----------------------------------------------------------------
def test_common_characters(text1, text2):
    common = set(text1).intersection(text2)
    return ''.join(common)

print test_common_characters("python", "code")

# -------------------------------------------------------------------
def test_remove_duplicate_characters(text1, text2):
    return ''.join(set(text1+text2))

print test_remove_duplicate_characters("python", "code")

# --------------------------------------------------------------------