# Part 1 is a set of coding problems solved with the use of list comprehension. The specific problems solved are detailed below.
# Part 2 is a set of coding problems solved with the use of higher order functions, an iterator, and a generator.
# At the end of the document, there are tests for each coding problem. There are test functions for Part 1 and doctests for Part 2.



# ========= PART 1 ================


# Vector plus one: takes in a 1d list of numbers (a vector) and outputs a 1d list of those numbers plus one.

vector_plus_one = lambda seq: [num+1 for num in seq]

# Collatz steps: Only for positive integers (not floats), the collatz steps are performed. That is, if the number is odd, the number
# is replaced with 3 times the number plus 1, and if the number is even, the number is replaced with 1/2 of the number. 

collatz_steps = lambda list: [3*n + 1 if n % 2 else n // 2 for n in filter(lambda item: isinstance(item, int) and item > 0, list)]

# Exchange matrix: given a number, an exchange matrix of that size is returned. An exchange matrix is a matrix with 1s all along
# the antidiagonal and 0s everywhere else, such as [[0,0,1],[0,1,0],[1,0,0]] for size 3.

exchange_matrix = lambda size: [[1 if i == size - 1 - j else 0 for i in range(size)] for j in range(size)]

# Get nonzero: given a 2d matrix, a list of tuples is returned, carrying the positions of nonzero entries.

get_nonzero = lambda matrix: [(i,j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] != 0]



# ========= PART 2 ================


# Given a function that has an input of a number and returns True or False, the higher-ordered function tests each digit
# against this function and multiplies all of the digits that return true. 1 is returned if none of the digits return True.

def mulDigits(num, fn):
    """
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
        >>> mulDigits(-494847464544434241, divByFour)
        8388608
    """
    result = 1
    num = abs(num)
    while num > 0:
        digit = num % 10   # Looking at last digit
        if fn(digit):
            result *= digit   # Calculate product of all digits that return True for fn
        num = num // 10       # Remove last digit
    return result


# Given a digit "x", this higher-ordered function returns a function that returns the number of digits in the number that match "x."

def getCount(x):
    """
        >>> getCount(6)(62156)
        2
        >>> digit = getCount(7)
        >>> digit(9457845778457077076)
        7
        >>> digit(-945784578457077076)
        6
        >>> getCount(6)(-65062156)
        3
    """
    
    def countfunc(num):
        num = abs(num)
        count = 0
        while num > 0:
            if num % 10 == x:
                count += 1
            num = num // 10
        return count

    return countfunc



# An iterator that is able to iterate through the input list both forwards and backwards through the use of "next" and ".reverse()". 

class Dual_Iterator:
    """
        >>> it = Dual_Iterator([2, 4, 6, 8, 10]) 
        >>> next(it)
        2
        >>> next(it)
        4
        >>> next(it)
        6
        >>> it.reverse()
        >>> next(it)
        4
        >>> next(it)
        2
        >>> next(it)
        10
        >>> it.reverse()
        >>> next(it)
        2
        >>> next(it)
        4
        >>> next(it)
        6
        >>> it.reverse()
        >>> next(it)
        4
        >>> next(it)
        2
        >>> next(it)
        10
        >>> next(it)
        8
        >>> next(it)
        6
        >>> it2 = Dual_Iterator([2, 4, 6, 8, 10]) 
        >>> [next(it2) for _ in range(12)]
        [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4]
        >>> it2.reverse()
        >>> [next(it2) for _ in range(12)]
        [2, 10, 8, 6, 4, 2, 10, 8, 6, 4, 2, 10]

        >>> it3 = Dual_Iterator([2, 4, 6, 8, 10])
        >>> it3.reverse()
        >>> next(it3)
        10
        >>> next(it3)
        8
    """
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = -1
        self.isReversing = False

    
    def __iter__(self):  # Do not modify
        return self

    
    def __next__(self):
        if not self.isReversing:
            self.index += 1
            if self.index > len(self.sequence) - 1:
                self.index = 0
        else:
            self.index -= 1
            if self.index < 0:
                self.index = len(self.sequence) - 1
        
        return self.sequence[self.index]


    def reverse(self):
        self.isReversing = not self.isReversing



# A generator function that replicates the "range" function in Python, but is able to utilize float values instead of only integers.

def frange(*args):
    '''
        >>> list(frange(7.5))
        [0, 1, 2, 3, 4, 5, 6, 7]
        >>> seq = frange(0,7, 0.1)
        >>> type(seq)
        <class 'generator'>
        >>> list(seq)
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]
        >>> list(seq)
        []
        >>> list(frange(0,7, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75]
        >>> list(frange(0,7.75, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5]
        >>> list(frange(0,7.75, -0.5))
        []
        >>> list(frange(7.75,0, -0.5))
        [7.75, 7.25, 6.75, 6.25, 5.75, 5.25, 4.75, 4.25, 3.75, 3.25, 2.75, 2.25, 1.75, 1.25, 0.75, 0.25]
    '''
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')

    current = start

    if step > 0:
        while current < stop:     # Counting up if step is positive
            yield current
            current = round(current + step,13)    # round to nearest trillionth to prevent issues with floats
    elif step < 0:
        while current > stop:     # Counting down if step is negative
            yield current
            current = round(current + step,13)
    else:
        raise TypeError('frange step size cannot = 0')




# ========= TESTING ASSERTIONS FOR PART 1 ================

def test_vector_plus_one():
    assert vector_plus_one([1, 2, 3]) == [2, 3, 4]
    assert vector_plus_one([0, 0, 0]) == [1, 1, 1]
    assert vector_plus_one([-1, -2, -3, -4, -5]) == [0, -1, -2, -3, -4]
    assert vector_plus_one([]) == []
    print('All cases for vector_plus_one passed!')

def test_collatz_steps():
    assert collatz_steps([1, 2, 3, 4]) == [4, 1, 10, 2]
    assert collatz_steps([0, "", -2, 1.5, 2.0]) == []
    assert collatz_steps([-1, -2, -3, -4, -5]) == []
    assert collatz_steps([]) == []
    print('All cases for collatz_steps passed!')


def test_exchange_matrix():
    assert exchange_matrix(1) == [[1]]
    assert exchange_matrix(2) == [[0, 1], [1, 0]]
    assert exchange_matrix(3) == [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    print('All cases for exchange_matrix passed!')


def test_get_nonzero():
    assert get_nonzero([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) == [(0, 0), (1, 1), (2, 2)]
    assert get_nonzero([[-1, 0, 0], [0, 0, 0], [0, 0, -3]]) == [(0, 0), (2, 2)]
    assert get_nonzero([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == []
    print('All cases for get_non_zero passed!')


# ========= TESTING ================

def run_tests():
    # Part 1
    #-- Uncomment each test function
    #test_vector_plus_one()
    #test_collatz_steps()
    #test_exchange_matrix()
    #test_get_nonzero()

    # Part 2
    import doctest    
    # -- Run tests per function - Uncomment the next line to run doctest by function. Replace mulDigits with the name of the function you want to test
    #doctest.run_docstring_examples(mulDigits, globals(), name='CodingProblems',verbose=True) 
    #doctest.testmod(verbose=True)  

# Uncomment to run tests
#if __name__ == "__main__":
    #run_tests()
