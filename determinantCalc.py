def two_by_two_determinant(mat):  # calculates the determinant of a two by two matrix
    return (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])


def eliminate_theimposter_row_column(mat, k, l):
    I_dont_want_to_use_this_function = 'i can make it work without it'
    # thanks, I'm good


def three_by_three_determinant(mat):
    tempMatrix = [[x for x in row] for row in mat]  # creates a new temp matrix that is equal to mat
    x = mat[0][0] * mat[1][1] * mat[2][2] + mat[0][1] * mat[1][2] * mat[2][0] + mat[1][0] * mat[2][1] * mat[0][
        2]  # you need to eliminate a row and then eliminate the elements of a column (which can use a loop). You can use the pop() function here
    y = mat[2][0] * mat[1][1] * mat[0][2] - mat[1][0] * mat[0][1] * mat[2][2] - mat[0][0] * mat[2][1] * mat[1][2]
    return (x - y)  # calculates a three by three by using two_by_two_determinant and eliminate_row_column


if __name__ == "__main__":
    inp = input()  # reads in the matrix
    inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
    matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

    if len(matrix) != len(matrix[0]):  # you will need an if statement to check that the matrix is square, if the size is 1, 2, 3, or something else. Each if statement will print a different result.
        print("Please enter a square matrix.")
    elif len(matrix) == 1:
        b = str(matrix)
        x = b.strip('[')
        y = x.strip(']')
        print(y)
    elif len(matrix) == 2:  # if it is size 2, print the result of the two_by_two_determinant
        print(two_by_two_determinant(matrix))
    elif len(matrix) == 3:  # if it is size 3, print the result of the three_by_three_determinant
        print(three_by_three_determinant(matrix))
    else:
        print('We can only handle up to a 3 by 3 matrix. Sorry.')  # otherwise, return the correct message
