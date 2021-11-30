string_1 = "PAYPALISHIRING"

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""



def conversion_repr(string_name, num_rows):
    string_len = len(string_name)
    # number of colums filled with single elements
    num_single_col_between = num_rows - 2

    # Remaining columns are filled with remaining elements
    num_full_col = len(string_name)num_rows



x = conversion_repr("PAYPALISHIRING", 4)
print(x)
