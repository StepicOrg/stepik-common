import random
import collections


def rand_N(N, low=0.8):
    return max(1, random.randint(int(low * N), N))


def equal_int(reply, clue):
    return int(reply) == int(clue)


def equal_ints(reply, clue):
    return [int(x) for x in reply.split()] == [int(x) for x in clue.split()]


def equal_float(reply, clue, precision=3):
    answer = float(reply)
    output = float(clue)
    return abs(reply - clue) < 0.1 ** precision + 1e-6


def equal_floats(reply, clue, precision=3):
    reply = [float(x) for x in reply.split()]
    clue = [float(x) for x in clue.split()]
    if len(reply) != len(clue):
        return False
    return all(abs(x - y) < 0.1 ** precision + 1e-6 for (x, y) in zip(reply, clue))


def equal_string_multiset(reply, clue):
    answer = collections.Counter(reply.split())
    output = collections.Counter(clue.split())
    return answer == output


def equal_int_multiset(reply, clue):
    reply = collections.Counter(int(x) for x in reply.split())
    clue = collections.Counter(int(x) for x in clue.split())
    return reply == clue


def nice(*args):
    """Format args nicely.

    >>> nice("foo")
    'foo'
    >>> nice("foo", 42)
    'foo\\n42'
    >>> nice([1,2,3], [4,5,6])
    '1 2 3\\n4 5 6'
    """
    def flat_nice(x):
        if isinstance(x, list):
            return ' '.join(map(str, x))
        else:
            return str(x)
    return '\n'.join(map(flat_nice, args))
    
    
# TODO: move to separate module
# Useful stuff for Data Analysis course

# Fisher's Iris Data
# (Sepal length, Sepal width, Petal length, Petal width, Species)
# from http://en.wikipedia.org/wiki/Iris_flower_data_set

IRIS_DATA = [
    (5.1, 3.5, 1.4, 0.1, 'I.setosa'),
    (4.9, 3.0, 1.4, 0.2, 'I.setosa'),
    (4.7, 3.2, 1.3, 0.2, 'I.setosa'),
    (4.6, 3.1, 1.5, 0.2, 'I.setosa'),
    (5.0, 3.6, 1.4, 0.2, 'I.setosa'),
    (5.4, 3.9, 1.7, 0.4, 'I.setosa'),
    (4.6, 3.4, 1.4, 0.3, 'I.setosa'),
    (5.0, 3.4, 1.5, 0.2, 'I.setosa'),
    (4.4, 2.9, 1.4, 0.2, 'I.setosa'),
    (4.9, 3.1, 1.5, 0.1, 'I.setosa'),
    (5.4, 3.7, 1.5, 0.2, 'I.setosa'),
    (4.8, 3.4, 1.6, 0.2, 'I.setosa'),
    (4.8, 3.0, 1.4, 0.1, 'I.setosa'),
    (4.3, 3.0, 1.1, 0.1, 'I.setosa'),
    (5.8, 4.0, 1.2, 0.2, 'I.setosa'),
    (5.7, 4.4, 1.5, 0.4, 'I.setosa'),
    (5.4, 3.9, 1.3, 0.4, 'I.setosa'),
    (5.1, 3.5, 1.4, 0.3, 'I.setosa'),
    (5.7, 3.8, 1.7, 0.3, 'I.setosa'),
    (5.1, 3.8, 1.5, 0.3, 'I.setosa'),
    (5.4, 3.4, 1.7, 0.2, 'I.setosa'),
    (5.1, 3.7, 1.5, 0.4, 'I.setosa'),
    (4.6, 3.6, 1.0, 0.2, 'I.setosa'),
    (5.1, 3.3, 1.7, 0.5, 'I.setosa'),
    (4.8, 3.4, 1.9, 0.2, 'I.setosa'),
    (5.0, 3.0, 1.6, 0.2, 'I.setosa'),
    (5.0, 3.4, 1.6, 0.4, 'I.setosa'),
    (5.2, 3.5, 1.5, 0.2, 'I.setosa'),
    (5.2, 3.4, 1.4, 0.2, 'I.setosa'),
    (4.7, 3.2, 1.6, 0.2, 'I.setosa'),
    (4.8, 3.1, 1.6, 0.2, 'I.setosa'),
    (5.4, 3.4, 1.5, 0.4, 'I.setosa'),
    (5.2, 4.1, 1.5, 0.1, 'I.setosa'),
    (5.5, 4.2, 1.4, 0.2, 'I.setosa'),
    (4.9, 3.1, 1.5, 0.2, 'I.setosa'),
    (5.0, 3.2, 1.2, 0.2, 'I.setosa'),
    (5.5, 3.5, 1.3, 0.2, 'I.setosa'),
    (4.9, 3.6, 1.4, 0.1, 'I.setosa'),
    (4.4, 3.0, 1.3, 0.2, 'I.setosa'),
    (5.1, 3.4, 1.5, 0.2, 'I.setosa'),
    (5.0, 3.5, 1.3, 0.3, 'I.setosa'),
    (4.5, 2.3, 1.3, 0.3, 'I.setosa'),
    (4.4, 3.2, 1.3, 0.2, 'I.setosa'),
    (5.0, 3.5, 1.6, 0.6, 'I.setosa'),
    (5.1, 3.8, 1.9, 0.4, 'I.setosa'),
    (4.8, 3.0, 1.4, 0.3, 'I.setosa'),
    (5.1, 3.8, 1.6, 0.2, 'I.setosa'),
    (4.6, 3.2, 1.4, 0.2, 'I.setosa'),
    (5.3, 3.7, 1.5, 0.2, 'I.setosa'),
    (5.0, 3.3, 1.4, 0.2, 'I.setosa'),
    (7.0, 3.2, 4.7, 1.4, 'I.versicolor'),
    (6.4, 3.2, 4.5, 1.5, 'I.versicolor'),
    (6.9, 3.1, 4.9, 1.5, 'I.versicolor'),
    (5.5, 2.3, 4.0, 1.3, 'I.versicolor'),
    (6.5, 2.8, 4.6, 1.5, 'I.versicolor'),
    (5.7, 2.8, 4.5, 1.3, 'I.versicolor'),
    (6.3, 3.3, 4.7, 1.6, 'I.versicolor'),
    (4.9, 2.4, 3.3, 1.0, 'I.versicolor'),
    (6.6, 2.9, 4.6, 1.3, 'I.versicolor'),
    (5.2, 2.7, 3.9, 1.4, 'I.versicolor'),
    (5.0, 2.0, 3.5, 1.0, 'I.versicolor'),
    (5.9, 3.0, 4.2, 1.5, 'I.versicolor'),
    (6.0, 2.2, 4.0, 1.0, 'I.versicolor'),
    (6.1, 2.9, 4.7, 1.4, 'I.versicolor'),
    (5.6, 2.9, 3.6, 1.3, 'I.versicolor'),
    (6.7, 3.1, 4.4, 1.4, 'I.versicolor'),
    (5.6, 3.0, 4.5, 1.5, 'I.versicolor'),
    (5.8, 2.7, 4.1, 1.0, 'I.versicolor'),
    (6.2, 2.2, 4.5, 1.5, 'I.versicolor'),
    (5.6, 2.5, 3.9, 1.1, 'I.versicolor'),
    (5.9, 3.2, 4.8, 1.8, 'I.versicolor'),
    (6.1, 2.8, 4.0, 1.3, 'I.versicolor'),
    (6.3, 2.5, 4.9, 1.5, 'I.versicolor'),
    (6.1, 2.8, 4.7, 1.2, 'I.versicolor'),
    (6.4, 2.9, 4.3, 1.3, 'I.versicolor'),
    (6.6, 3.0, 4.4, 1.4, 'I.versicolor'),
    (6.8, 2.8, 4.8, 1.4, 'I.versicolor'),
    (6.7, 3.0, 5.0, 1.7, 'I.versicolor'),
    (6.0, 2.9, 4.5, 1.5, 'I.versicolor'),
    (5.7, 2.6, 3.5, 1.0, 'I.versicolor'),
    (5.5, 2.4, 3.8, 1.1, 'I.versicolor'),
    (5.5, 2.4, 3.7, 1.0, 'I.versicolor'),
    (5.8, 2.7, 3.9, 1.2, 'I.versicolor'),
    (6.0, 2.7, 5.1, 1.6, 'I.versicolor'),
    (5.4, 3.0, 4.5, 1.5, 'I.versicolor'),
    (6.0, 3.4, 4.5, 1.6, 'I.versicolor'),
    (6.7, 3.1, 4.7, 1.5, 'I.versicolor'),
    (6.3, 2.3, 4.4, 1.3, 'I.versicolor'),
    (5.6, 3.0, 4.1, 1.3, 'I.versicolor'),
    (5.5, 2.5, 4.0, 1.3, 'I.versicolor'),
    (5.5, 2.6, 4.4, 1.2, 'I.versicolor'),
    (6.1, 3.0, 4.6, 1.4, 'I.versicolor'),
    (5.8, 2.6, 4.0, 1.2, 'I.versicolor'),
    (5.0, 2.3, 3.3, 1.0, 'I.versicolor'),
    (5.6, 2.7, 4.2, 1.3, 'I.versicolor'),
    (5.7, 3.0, 4.2, 1.2, 'I.versicolor'),
    (5.7, 2.9, 4.2, 1.3, 'I.versicolor'),
    (6.2, 2.9, 4.3, 1.3, 'I.versicolor'),
    (5.1, 2.5, 3.0, 1.1, 'I.versicolor'),
    (5.7, 2.8, 4.1, 1.3, 'I.versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'I.virginica'),
    (5.8, 2.7, 5.1, 1.9, 'I.virginica'),
    (7.1, 3.0, 5.9, 2.1, 'I.virginica'),
    (6.3, 2.9, 5.6, 1.8, 'I.virginica'),
    (6.5, 3.0, 5.8, 2.2, 'I.virginica'),
    (7.6, 3.0, 6.6, 2.1, 'I.virginica'),
    (4.9, 2.5, 4.5, 1.7, 'I.virginica'),
    (7.3, 2.9, 6.3, 1.8, 'I.virginica'),
    (6.7, 2.5, 5.8, 1.8, 'I.virginica'),
    (7.2, 3.6, 6.1, 2.5, 'I.virginica'),
    (6.5, 3.2, 5.1, 2.0, 'I.virginica'),
    (6.4, 2.7, 5.3, 1.9, 'I.virginica'),
    (6.8, 3.0, 5.5, 2.1, 'I.virginica'),
    (5.7, 2.5, 5.0, 2.0, 'I.virginica'),
    (5.8, 2.8, 5.1, 2.4, 'I.virginica'),
    (6.4, 3.2, 5.3, 2.3, 'I.virginica'),
    (6.5, 3.0, 5.5, 1.8, 'I.virginica'),
    (7.7, 3.8, 6.7, 2.2, 'I.virginica'),
    (7.7, 2.6, 6.9, 2.3, 'I.virginica'),
    (6.0, 2.2, 5.0, 1.5, 'I.virginica'),
    (6.9, 3.2, 5.7, 2.3, 'I.virginica'),
    (5.6, 2.8, 4.9, 2.0, 'I.virginica'),
    (7.7, 2.8, 6.7, 2.0, 'I.virginica'),
    (6.3, 2.7, 4.9, 1.8, 'I.virginica'),
    (6.7, 3.3, 5.7, 2.1, 'I.virginica'),
    (7.2, 3.2, 6.0, 1.8, 'I.virginica'),
    (6.2, 2.8, 4.8, 1.8, 'I.virginica'),
    (6.1, 3.0, 4.9, 1.8, 'I.virginica'),
    (6.4, 2.8, 5.6, 2.1, 'I.virginica'),
    (7.2, 3.0, 5.8, 1.6, 'I.virginica'),
    (7.4, 2.8, 6.1, 1.9, 'I.virginica'),
    (7.9, 3.8, 6.4, 2.0, 'I.virginica'),
    (6.4, 2.8, 5.6, 2.2, 'I.virginica'),
    (6.3, 2.8, 5.1, 1.5, 'I.virginica'),
    (6.1, 2.6, 5.6, 1.4, 'I.virginica'),
    (7.7, 3.0, 6.1, 2.3, 'I.virginica'),
    (6.3, 3.4, 5.6, 2.4, 'I.virginica'),
    (6.4, 3.1, 5.5, 1.8, 'I.virginica'),
    (6.0, 3.0, 4.8, 1.8, 'I.virginica'),
    (6.9, 3.1, 5.4, 2.1, 'I.virginica'),
    (6.7, 3.1, 5.6, 2.4, 'I.virginica'),
    (6.9, 3.1, 5.1, 2.3, 'I.virginica'),
    (5.8, 2.7, 5.1, 1.9, 'I.virginica'),
    (6.8, 3.2, 5.9, 2.3, 'I.virginica'),
    (6.7, 3.3, 5.7, 2.5, 'I.virginica'),
    (6.7, 3.0, 5.2, 2.3, 'I.virginica'),
    (6.3, 2.5, 5.0, 1.9, 'I.virginica'),
    (6.5, 3.0, 5.2, 2.0, 'I.virginica'),
    (6.2, 3.4, 5.4, 2.3, 'I.virginica'),
    (5.9, 3.0, 5.1, 1.8, 'I.virginica')]
