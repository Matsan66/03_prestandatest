import random

def generate_random_list(size, max_value):
    """
    Function to generate q list with random numbers
    :param size:
    :return:
    """
    return [random.randint(0, max_value) for _ in range(size)]