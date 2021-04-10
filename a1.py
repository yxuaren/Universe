def is_multiple_of_11(n):
    """Return True if n is a multiple of 11; False otherwise."""
    if n % 11 == 0:
        return True
    return False

def last_prime(m):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    def check_prime(k):
        for i in range(2, round(k ** 0.5)+1):
            if k % i == 0:
                return False
        return True
    assert(m >= 1)
    if m == 1:
        return False
    if m <= 3:
        return m
    if m % 2 ==0:
        m = m - 1
    for i in range(m, 1, -2):
        if check_prime(i):
            return i

def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    if a==0:
        x = -c / b
        return (x, x)
    delta = b**2 - 4*a*c
    if delta < 0:
        return 'complex'
    else:
        return ((-b - delta**0.5)/(2*a), (-b + delta**0.5)/(2*a))

def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    For example, [0, 1, 2, 3, 4, 5, 6, 7] => [0, 4, 1, 5, 2, 6, 3, 7]"""
    length = len(even_list)
    half_length = int(length/2)
    shuffle = []
    for i in range(half_length):
        shuffle.append(even_list[i])
        shuffle.append(even_list[i+half_length])
    return shuffle

def five_times_list(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 5."""
    return [5*i for i in input_list]


def triple_vowels(text):
    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are 
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    results = ''
    for i in text:
        if i in vowels:
            results = results + 3*i
        else:
            results = results + i
    return results


def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""
    text = text.lower().split()
    dic = {}
    for word in text:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] = dic[word] + 1
    return dic


def make_quartic_evaluator(a, b, c, d, e):
    """When called with 5 numbers, returns a function of one variable (x)
    that evaluates the quartic polynomial
    a x^4 + b x^3 + c x^2 + d x + e.
    For this exercise Your function definition for make_quartic_evaluator 
    should contain a lambda expression."""
    quartic_polynomial = lambda x: a*x**4 + b*x**3 + c*x**2 + d*x +e
    return quartic_polynomial


class Polygon:
    """Polygon class."""
