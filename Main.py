import random

print("\nThere are multiple ways to generate pseudo-random numbers. They are pseudo-random because it is possible to "
      "reroll the same number/sequence.")

print("\nUsing .random will generate a float value between 0 and 1.")
a = random.random()
print(a)

print("\nIt is possible to have a float in a certain range with the endpoint included using .uniform().")
a = random.uniform(1, 10)
print(a)

print("\nIt is possible to have an int in a certain range with the endpoint included using .randint().")
a = random.randint(1, 10)
print(a)

print("\nIt is possible to have an int in a certain range with the endpoint excluded using .randrange().")
a = random.randrange(1, 10)
print(a)

print("\nIt is possible to generate a float using the mean and standard deviation using .normalvariate().")
a = random.normalvariate(0, 1)
print(a)

print("\nIt is also possible to use random functions with sequences, such as lists.")
mylist = list("ABCDEFGH")

print("\nIt is possible to have a random element in a list be chosen using .choice().")
a = random.choice(mylist)
print(a)

print("\nIt is possible to have a few elements chosen at once with no repeats using .sample().")
a = random.sample(mylist, 3)
print(a)

print("\nIt is possible to have a few elements chosen at once with possible repeats using .choices().")
a = random.choices(mylist, k=3)
print(a)

print("\nIt is possible to shuffle a list using .shuffle().")
random.shuffle(mylist)
print(mylist)

print("\nIt is possible to repeat the random values using a seed, thus it is not recommended for security reasons.")
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

print("\nIt is recommended to use a module like secrets for security purposes for a true random value.")
import secrets

print("\nUsing .randbelow() will generate an int below the max value stated.")
a = secrets.randbelow(10)
print(a)

print("\nUsing .randbits() will generate a desired amount of bits, i.e. putting 4 will generate a number with "
      "4 bits (i.e. 1011)")
a = secrets.randbits(4) #The max value of 4 bits is 1111 which is 15.
print(a)

print("\nIt is possible to choose a random element in a list using .choice().")
a = secrets.choice(mylist)
print(a)

print("\nIt is possible to generate random set of elements in an array using functions from the numpy module.")
import numpy as np

print("\nIt is possible to generate a list of floats using .random.rand().")
arr = np.random.rand(3)
print(arr)

print("\nIt is also possible to generate a list of integers in a range instead of floats using randint().")
arr = np.random.randint(3, 10, 3)
print(arr)

print("\nIt is also possible to generate a multi-dimensional array.")
arr = np.random.randint(0, 10, (3,3))
print(arr)

print("\nIt is possible to shuffle a multi-dimensional array, however it will only shuffle the numbers in the same "
      "column.")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

print("\nnumpy has it's own number generation and seed method compared to the regular random module. It is recommended "
      "use the numpy version instead when able.")
np.random.seed(1)
print(np.random.randint(0, 3, (3, 3)))
np.random.seed(1)
print(np.random.randint(0, 3, (3, 3)))