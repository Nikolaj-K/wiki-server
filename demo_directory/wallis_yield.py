"""
https://en.wikipedia.org/wiki/List_of_formulae_involving_%CF%80
"""

import math
import time
from fractions import Fraction as ratio


def _leibniz_sum_stream():
    # https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    # math.pi/4 = 0.78539...
    s = 0 # sum
    # s=0, s=0+1, s=0+1-1/3, s=0+1-1/3+1/5, s=....
    sign = 1
    n = 0
    while True:
        yield 4 * s # the Leibnitz sum computes pi / 4
        denom = 2 * n + 1
        s += ratio(sign, denom)
        sign *= -1
        n += 1


def _wallis_product_stream():
    # https://en.wikipedia.org/wiki/Wallis_product
    p = 1 # product
    n = 1
    while True:
        yield 2 * p # the Wallis product computes pi / 2
        num_n = 4 * n**2
        p *= ratio(num_n, num_n - 1)
        n += 1


def _wallis_product_stream_num_denom_stream():
    p_num = 1
    p_denom = 1
    n = 1
    while True:
        yield n, 2 * p_num, p_denom
        num = 4 * n**2
        p_num *= num
        p_denom *= (num - 1)
        #p_gcd = math.gcd(p_num, p_denom) # tends to kill off only a few digits
        #p_num = p_num // p_gcd
        #p_denom = p_denom // p_gcd
        n += 1


def main_pi():
    joint_stream = zip(
        _leibniz_sum_stream(),
        _wallis_product_stream(),
        _wallis_product_stream_num_denom_stream()
    )

    for s, p, (n, num, denom) in joint_stream:
        print(f"\ncounter: n={n}\nleibniz: {float(s)}\nwallis : {float(p)}\nmath.pi: {math.pi}")
        print(p)
        assert num == denom * p
        time.sleep(.3)


def _eval_series(term_function, number_stream):
    # Note: term_function and number_stream are expected to have fitting argument and return value patterns
    for (n, num, denom) in number_stream():
        yield n, sum(term_function(k, num, denom) for k in range(n))


def _cos_term(k, num, denom):
    # https://en.wikipedia.org/wiki/Trigonometric_functions#Power_series_expansion
    x = ratio(num, denom)
    j = 2 * k
    t = (-1)**k * x**j / int(math.factorial(j))
    return t


def main_cos_of_pi():
    cos_of_pi_stream = _eval_series(_cos_term, _wallis_product_stream_num_denom_stream)
    # Anayltically, cos(pi) == -1, so this sequence is in the Cauchy real -1

    for n, y in cos_of_pi_stream:
        print(f"\ncount: {n}\ncos_of_pi: {float(y)}")
        #print(f"as a rational: {y}")
        time.sleep(1)


main_pi()
main_cos_of_pi()
