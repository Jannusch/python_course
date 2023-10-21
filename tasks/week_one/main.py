from math import factorial

def simple_arithmetic():
    # Try to solve the following problem:
    # 1.5 + 5

    # The variable 'a' gets the value of 1.5 assigned to it.
    a = 1.5

    # Now a + b is calculated and the result is stored in the variable 'c'.

    # Finally, the result is printed to the console.

    # This line is for the test. I will explain later what it does.
    return c

def simple_volume():
    # The volume of a cube should be calculated.
    # The length of a side is defined in the variable 'side_length'.
    # The length of a side is 15 cm.
    # The result should be stored in the variable 'volume'.


    # This line is for the test. I will explain later what it does.
    return volume, side_length

def simple_volume_2():
    # Try the same but for a pyramid.
    # Length of first side is 15 cm.
    # Length of second side is 10 cm.
    # Height is 20 cm.

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
    # Replace the None with your solution.
    combinations = None

    # and for 23 persons
    combinations_23 = None

    # Out of this combinations, we are only interested in the combinations where the birthdays are NOT the same.
    # For the first person we have 365 possibilities.
    # For the second person we have 364 possibilities left, etc.
    # Hint: n! is in python factorial(n)
    different_birthdays = None

    # Now we can use the Laplace formula to calculate the probability that all persons have different birthdays.
    probability = None

    # The probability that two persons have the same birthday is the complement of the probability that all persons have different birthdays.
    probability_complement = None

    # Print your result to the console.

    # This line is for the test. I will explain later what it does.
    return combinations, different_birthdays, probability, probability_complement

if __name__ == '__main__':
    simple_arithmetic()
    simple_volume()
    birthday()
