'''
Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using 
the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 

Examples: 

    Input: n = 4
    Output: 5

    Explanation:

    For a 2 x 4 board, there are 5 ways

        All 4 vertical (1 way)
        All 4 horizontal (1 way)
        2 vertical and 2 horizontal (3 ways)

    Input: n = 3

    Output: 3

    Explanation:

    We need 3 tiles to tile the board of size  2 x 3.

    We can tile the board using following ways

        Place all 3 tiles vertically.
        Place 1 tile vertically and remaining 2 tiles horizontally (2 ways)
'''
def tiling(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return b

print(tiling(30))