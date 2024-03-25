def echelon_calculator(mat):    #You need to copy in your Echelon Calculator, but modify it to keep track of the number of row switches.
    i = 0                              #The echelon calculator will need to return the matrix in echelon form and the number of switches.
    j = 0
    x = 0
    while j < C:
        zero_location = under_nonzero_finder(mat,j,i)
        if zero_location == r + 1:
            j += 1
        elif zero_location > i:
            temp_row = mat[zero_location]
            mat[zero_location] = mat[i]
            mat[i] = temp_row
            x += 1
        else:
            for l in range(i+1, r):
                a = (mat[l][j]/mat[i][j])
                mat[l] = subtract_row_times_num_to_row(mat[i],mat[l],a)
            j += 1
            i += 1
    return mat, x
def determinant_calculator_echelon(mat):
    det = 1 #initial for det
    echelon_calculator(mat,x)
    for num in mat:
        det = det*mat[num][num]#this needs to turn the matrix into echelon form and then use it to calculate the matrix
    if det == -0.0:     #to fix the strange -0.0 case that happens in the echelon form calculator. You can also fix this in the echelon calculator
        det = 0.0
    return det
if __name__ == "__main__":
    inp = input()  # reads in the matrix
    inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
    matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input


       #enter the correct print statements.