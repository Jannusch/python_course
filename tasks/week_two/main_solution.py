########################## Helper functions - Main Tasks a few lines down ##################

# class for points to easy excess the x and y coordinate
class point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# lists that contain all the points after reading
cluster_one = []
cluster_two = []
unclassified_points = []
data_points = []


# This is a helper function
# You can read it and try to understand it but for now this is not necessary.
# We will later discuss everything step by step
def read_data():
    # empty the lists to make sure that they are empty
    cluster_one.clear()
    cluster_two.clear()
    unclassified_points.clear()
    data_points = []

    # open the file with read only permission
    f = open("Data.txt", "r")
    print("Start reading")
    # iterate over all lines and extract from each line the point
    index = 0
    for line in f.readlines():
        # split each line at the whitespace to separate the x and y coordinate
        x_y = line.split(" ")
        # create a data object out of the points. Convert explicitly to float because file contains
        # scientific notation
        if index < 100:
            cluster_one.append(point(float(x_y[1]), float(x_y[2])))
        elif index < 200:
            cluster_two.append(point(float(x_y[1]), float(x_y[2])))
        else:
            unclassified_points.append(point(float(x_y[1]), float(x_y[2])))
        index += 1
    data_points = cluster_one + cluster_two

########################### The main task starts here #####################################

### First Task ###

def fibonacci():
    # calculate the 12th fibonacci number
    # You can also try some other numbers, for the test 12 is relevant.
    number = None

    a = 0   
    b = 1
    c = 1

    # even though the task says 12th fibonacci number, we only need to iterate 11 times.
    # because we already have the first two numbers defined.
    for i in range(11):
        c = a + b
        a = b
        b = c
    print(c)
    number = c

    return number

def fibonacci_two():
    # Calculate the fibonacci number until the number is higher than 1337
    # Save the number of iterations needed to reach 1337 in the variable number
    
    a = 0   
    b = 1
    c = 1

    number = None

    for i in range(100):
        c = a + b
        a = b
        b = c
        # this line checks if we have reached 1337 and if we have not already found a number
        # Python has an inbuilt function to break a loop. Its called "break" (who could have guessed that)
        if c > 1337 and number == None:
            number = i
    # now we have add one to the number because our for loop starts at zero
    print (number + 1)

    # This for loop uses the break inside the loop
    # But first we have to reset the variables
    a = 0   
    b = 1
    c = 1
    for i in range(100):
        c = a + b
        a = b
        b = c
        if c > 1337:
            number = i
            # after this line is executed the loop will end
            break

    print (number + 1)
    return number

### Second Task ###
# For the second task some help is needed to solve it efficiently.
# Three data structures are given:
# 1. One that contains all the points from cluster one (cluster_one).
# 2. One that contains all the points from cluster two (cluster_two).
# 3. One that contains all the points we try to classify.
# You can look at the top of this file to see how the data is stored in the data structure. But for now its not important.
# You can iterate over the data structure with a for loop.
# 
# for point in data_points:
#    do something with point
#
# Each element has a x and a y coordinate. 
# You can access it with point.x and point.y (and point is the variable you used in the for loop).
# The length of the data structure can be accessed with len(data_points).

def means():
    # The first step is to calculate the mean of each cluster.
    mean_c1 = 0
    mean_c2 = 0

    for point in cluster_one:
        mean_c1 += (point.x**2 + point.y**2) ** 0.5
    mean_c1 = mean_c1 / len(cluster_one)

    for point in cluster_two:
        mean_c2 += (point.x**2 + point.y**2) ** 0.5
    mean_c2 = mean_c2 / len(cluster_two)


    # print the mean of each cluster
    print("Means:", mean_c1, mean_c2)

    # The second step is to calculate the mean of both means.
    mean = 0
    mean = (mean_c1 + mean_c2) / 2

    # print the mean of both means
    print("Mean of both means:", mean)
    # This line "transfers" the variables to the classify function
    return mean_c1, mean_c2, mean  
    

def classify():
    # Next week we will learn what this line does
    # But for now you only need to know that you can use your means from the last step
    mean_c1, mean_c2, mean = means()


    # The third step is to classify the unclassified points.
    # Simply check if the distance to the mean of cluster one is smaller than the distance to the mean of cluster two.
    # You can add the point to cluster_one/two with cluster_one.append(point)
    # Finally print the length of each cluster  


    for point in unclassified_points:
        if (point.x**2 + point.y**2) ** 0.5 >= mean:
            cluster_one.append(point)
        else:
            cluster_two.append(point)
    
    print("Length of cluster one:", len(cluster_one))
    print("Length of cluster two:", len(cluster_two))


    return len(cluster_one), len(cluster_two)


def threshold():
    # This task is the most difficult one. But you can do it!
    # This is one of the basic classification algorithms. It separates the data into two clusters divided by a line.
    # The line is defined by two points: (-2, 6) and (6, -2)
    # We need the perpendicular vector w to this line to calculate the distance of the points to the line.
    # You can use the same data structures as in the last task.

    x = -2 -6
    y = 6 - -2
    print(f"Line: ({x}, {y})")

    # The following code calculates the orthogonal vector to the line with the Gram-Schmidt algorithm.
    
    # dot product of point one and line
    sk_1 = x * -2 + y * 6

    # dot product of line with line
    sk_2 = x * x + y * y

    # fraction of dot products
    fraction = sk_1 / sk_2

    # fraction with line
    x_tmp = fraction * x
    y_tmp = fraction * y

    # orthogonal vector
    x_final = -2 - x_tmp
    y_final = 6 - y_tmp

    # And finally normalize the vector
    length = (x_final**2 + y_final**2) ** 0.5
    x_final = x_final / length
    y_final = y_final / length

    # Orthogonal vector is now (x_final, y_final)
    print(f"Orthogonal vector: ({x_final}, {y_final})")


    # We now search a threshold t that separates the data into two clusters.
    # We therefor search the max threshold under which w^T * x < t is true for all points in cluster one.
    t_max = 0

    for point in cluster_one:
        t = x_final * point.x + y_final * point.y
        if t > t_max:
            t_max = t
    print("Threshold:", t_max)

    # The las step is simply classifying the points with the threshold.
    # Again append it to the cluster with cluster_one.append(point)

    for point in unclassified_points:
        t = x_final * point.x + y_final * point.y
        if t > t_max:
            cluster_one.append(point)
        else:
            cluster_two.append(point)

    # And finally print the length of each cluster
    print("Length of cluster one:", len(cluster_one))
    print("Length of cluster two:", len(cluster_two))
    # Again one line for the test
    len_1 = len(cluster_one)
    len_2 = len(cluster_two)
    return len_1, len_2


if __name__ == "__main__":
    task = input("Which task do you want to run?\n\t1: Fibonacci\n\t2: Fibonacci 1337\n\t3: Baseline - Means\n\t4: Baseline - Classify\n\t5: Threshold\n")
    if task == "1":
        fibonacci()
    elif task == "2":
        fibonacci_two()
    elif task == "3":
        read_data()
        means()
    elif task == "4":
        read_data()
        classify()
    elif task == "5":
        read_data()
        threshold()
    else:
        print("Wrong input")