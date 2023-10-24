from math import factorial


def simple_arithmetic():
    # Try to solve the following problem:
    # 1.5 + 5

    # The variable 'a' gets the value of 1.5 assigned to it.
    a = 1.5
    b = 5
    # Now a + b is calculated and the result is stored in the variable 'c'.
    c = a + b
    # Finally, the result is printed to the console.
    print(c)

    # This line is for the test. I will explain later what it does.
    return c


def simple_volume():
    # The volume of a cube should be calculated.
    # The length of a side is defined in the variable 'side_length'.
    # The length of a side is 15 cm.
    # The result should be stored in the variable 'volume'.
    side_length = 15
    volume = side_length ** 3

    # This line is for the test. I will explain later what it does.
    return volume, side_length


def simple_volume_2():
    # Try the same but for a pyramid.
    # Length of first side is 15 cm.
    # Length of second side is 10 cm.
    # Height is 20 cm.
    volume = 15 * 10 * 20 / 3

    # This line is for the test. I will explain later what it does.
    return volume

def birthday():
    # The birthday problem is a famous probability problem.
    # The problem is as follows:
    # What is the probability that two people in a room have the same birthday?
    # We assume that the probability of being born on a specific day is 1/365.
    # The room has 23 people in it.
    # The final result should be stored in the variable 'probability_complement'.


    # The number of all possible combinations is 365^n with n = number of persons.
    # Calculate the combinations for 2 persons.
    combinations = 365 ** 2

    # and for 23 persons
    combinations_23 = 365 ** 23

    # Out of this combinations, we are only interested in the combinations where the birthdays are NOT the same.
    # For the first person we have 365 possibilities.
    # For the second person we have 364 possibilities left, etc.
    # Hint: n! is in python factorial(n)
    different_birthdays = factorial(365) / factorial(365 - 23)

    # Now we can use the Laplace formula to calculate the probability that all persons have different birthdays.
    probability = different_birthdays / combinations_23

    # The probability that two persons have the same birthday is the complement of the probability that all persons have different birthdays.
    probability_complement = 1 - probability

    # Print your result to the console.
    print(probability_complement)
    # This line is for the test. I will explain later what it does.
    return combinations, different_birthdays, probability, probability_complement

def advanced_arithmetic():
    # This task should prepare you for the next weeks.
    # The first task is to calculate the euclidean distance between two points.
    # The points are (2, 4) and (5, 8).
    # The result should be stored in the variable 'distance'.
    distance = ((2 - 5) ** 2 + (4 - 8) ** 2) ** 0.5

    # The second step is the distance between two points in 3D.
    # The points are (2, 4, 6) and (5, 8, 10).
    distance_3d = ((2 - 5) ** 2 + (4 - 8) ** 2 + (6 - 10) ** 2) ** 0.5

    # The third step is the distance in a 8-dimensional space. (Don't worry, you don't have to imagine it.)
    # The points are (2, 4, 6, 8, 10, 12, 14, 16) and (5, 8, 10, 12, 14, 16, 18, 20).
    distance_8d = ((2 - 5) ** 2 + (4 - 8) ** 2 + (6 - 10) ** 2 + (8 - 12) ** 2 + (10 - 14) ** 2 + (12 - 16) ** 2 + (14 - 18) ** 2 + (16 - 20) ** 2) ** 0.5

    # Now we calculate the distance again in 8D but with the second point being (5, 8, 10, 12, 14, 16, 18, 200).
    distance_8d_2 = ((2 - 5) ** 2 + (4 - 8) ** 2 + (6 - 10) ** 2 + (8 - 12) ** 2 + (10 - 14) ** 2 + (12 - 16) ** 2 + (14 - 18) ** 2 + (16 - 200) ** 2) ** 0.5


    # Maybe you noticed something strange about the last two results.
    #
    #

     # *Spoiler*
    # What you discovered is called the curse of dimensionality.
    # Only the change of one dimension leads to a huge change in the distance.
    # This is a problem for machine learning algorithms.
    # Therefore different distance measures are used.
    # One of them is the cosine similarity.
    # Try to implement it. And maybe you can read something about the curse of dimensionality, it is very interesting.

    dot_product = 2 * 5 + 4 * 8 + 6 * 10 + 8 * 12 + 10 * 14 + 12 * 16 + 14 * 18 + 16 * 200
    norm_a = ((2 ** 2 + 4 ** 2 + 6 ** 2 + 8 ** 2 + 10 ** 2 + 12 ** 2 + 14 ** 2 + 16 ** 2) ** 0.5)
    norm_b = ((5 ** 2 + 8 ** 2 + 10 ** 2 + 12 ** 2 + 14 ** 2 + 16 ** 2 + 18 ** 2 + 200 ** 2) ** 0.5)
    distance_cosine = dot_product / (norm_a * norm_b)

    # This line is for the test. I will explain later what it does.
    return distance, distance_3d, distance_8d, distance_8d_2, distance_cosine

if __name__ == '__main__':
    simple_arithmetic()
    simple_volume()
    simple_volume_2()
    birthday()
    advanced_arithmetic()
