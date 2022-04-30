# Implementation of Linear Congruential Generator PRNG

class LCG():
    """
    generates as many random numbers, using a Linear Congruential Generator
    This uses the formula: X_(i+1) = (aX_i + c) mod m
    """

    def __init__(self):
        self.x_0 = 123456789.0        # Our seed, or X_value = 123456789
        self.a = 101427               # Our "a" base value
        self.c = 321                  # Our "c" base value
        self.m = (2 ** 16)            # Our "m" base value


    def random_array(self, NUMBER_OF_SAMPLES):
        """
        Generates the random values using the above formula
        """
        random_numbers = []

        for i in range(NUMBER_OF_SAMPLES): 
            # Store value of each iteration 
            self.x_0 = (self.a * self.x_0 + self.c) % self.m

            # Get the value in U[0, 1) by divide x_0 by m
            rand_val = self.x_0 / self.m

            # Append the value to list
            random_numbers.append(rand_val)

        return random_numbers