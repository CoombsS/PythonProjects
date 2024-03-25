def extended_vector(vec):    #this will turn any vector with less than 3 components into a 3-vector
    while len(vector1) < 3:
        vector1.append(0)
    while len(vector2) < 3:
        vector2.append(0)
    #add zero onto it
def cross_product(vec1,vec2):
    if len(vec1) == 3 and len(vec2) == 3:  #Verify that the vectors are the correct size
        cross_prod = [0,0,0]
        cross_prod[0] = vec1[1]*vec2[2]-vec1[2]*vec2[1]
        cross_prod[1] = vec1[2]*vec2[0]-vec1[0]*vec2[2]
        cross_prod[2] = vec1[0]*vec2[1]-vec1[1]*vec2[0]
        return cross_prod
    if len(vec1) < 3  or len(vec2) < 3:
        cross_prod = [0,0,0]
        extended_vector(vec1)#calculate the cross product components
        extended_vector(vec2)
        cross_prod[0] = vec1[1]*vec2[2]-vec1[2]*vec2[1]
        cross_prod[1] = vec1[2]*vec2[0]-vec1[0]*vec2[2]
        cross_prod[2] = vec1[0]*vec2[1]-vec1[1]*vec2[0]
        return cross_prod
    else:
        print("Please enter 2d or 3d vectors.")
                                    #If the vectors are not the right size, return the corect message.

if __name__ == "__main__":
    inpvec1 = input()  # reads in a vector
    vector1 = [float(t.strip("[](), ")) for t in inpvec1.split(",")]  # creates a list for the first vector

    inpvec2 = input()  # reads in a vector
    vector2 = [float(t.strip("[](), ")) for t in inpvec2.split(",")]  # creates a list for the second vector

    print(cross_product(vector1,vector2))
