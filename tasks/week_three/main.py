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


# The implementation of the fibonacci function is missing.
# The "solution" how to get the 12th fibonacci number is odd. We want to use the fibonacci function to calculate other fibonacci numbers, too.
# Add an argument and the return type.
def fibonacci():
    # calculate the 12th fibonacci number
    # You can also try some other numbers, for the test 12 is relevant.
    number = None
    return number

# The same thing as for the normal fibonacci function should be done here.
# You can use a for loop like last week or you can use a while loop.
# While loops are used when you don't know how often you need to iterate.
def fibonacci_two():
    # Calculate the fibonacci number until the number is higher than 1337
    # Save the number of iterations needed to reach 1337 in the variable number
    number = None
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
    # uh this sounds like a we have to do the same thing twice -> time for a function!
    # Define a function that calculates the mean of a cluster.
    mean_c1 = 0
    mean_c2 = 0


    # print the mean of each cluster

    # The second step is to calculate the mean of both means.
    mean = 0

    # print the mean of both means

    # The next line return the variables to the classify function
 
    

def classify():
    # Next week we will learn what this line does
    # No - this was last week. This week we will learn what this line does!
    # Oh but the line is missing. Ok. To classify the cluster we need the mean of each cluster and the mean of both means.
    # Luckily we have a function that returns all of them.



    # The third step is to classify the unclassified points.
    # Simply check if the distance to the mean of cluster one is smaller than the distance to the mean of cluster two.
    # You can add the point to cluster_one/two with cluster_one.append(point)
    # Finally print the length of each cluster  


    return len(cluster_one), len(cluster_two)


def threshold():
    # This task is the most difficult one. But you can do it!
    # This is one of the basic classification algorithms. It separates the data into two clusters divided by a line.
    # The line is defined by two points: (-2, 6) and (6, -2)
    # We need the perpendicular vector w to this line to calculate the distance of the points to the line.
    # You can use the same data structures as in the last task.
    # Hint: Gram-Schmidt process (https://de.wikipedia.org/wiki/Gram-Schmidtsches_Orthogonalisierungsverfahren)

    # The adaption for this week is, that we want to change the two points.
    # Also the part of calculating the line is not directly part of this task.
    # So define a function and call it in this function.
    # You have to define it outside of this function. (So the indentation is one level less than this function)


    # We now search a threshold t that separates the data into two clusters.
    # We therefor search the max threshold under which w^T * x < t is true for all points in cluster one.
    # Once again define this as a function.


    # The las step is simply classifying the points with the threshold.
    # Again append it to the cluster with cluster_one.append(point)
    # But with a function. Maybe you can adapt the classify function from the last task.

    # And finally print the length of each cluster

    # Again one line for the test
    return len(cluster_one), len(cluster_two)

# This line is the main entrY point of the program
# in detailed this will be explained in the week about packages
if __name__ == "__main__":
    # We - I mean you - need to fix this.
    # The program should ask which task to run and then run the task.
    # The error message should be helpful to solve this.

    task = input("Which task do you want to run?\n\t1: Fibonacci\n\t2: Fibonacci 1337\n\t3: Baseline - Means\n\t4: Baseline - Classify\n\t5: Threshold\n")
    
    if task == "1":
    elif task == "2":
    elif task == "3":
    elif task == "4":
    elif task == "5":
    else:
        print("Wrong input")