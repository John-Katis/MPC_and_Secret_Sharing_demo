# This code file contains blanks that are meant to be filled in!
#
# Where you see "# TODO", it means that you should write some code 
# to implement the protocol!
#
# The protocol steps are given within the function placeholders.
#
# -------------------------------------------------------------------------

import sys
from pathlib import Path

# Add parent directory (one level up) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from typing import List, Tuple
from math_helpers import P, addp, subp, mulp, gen_random_list, gen_random_num



# Points on which we evaluate the polynomial
# Since point 0 is the secret, we start from 1
def xs_range(n: int) -> List[int]:
    return list(range(1, n + 1))



# ------------------------------------------------------------------
# Shamir share
# ------------------------------------------------------------------
def share_secret(secret: int, n: int, t: int, xs=None) -> Tuple[List[int], List[int]]:
    if xs is None:
        xs = xs_range(n)

    # generate t+1 coefficients, t random and the secret
    coeffs = [secret] + gen_random_list(0, 10**6, t)  # secret is coeff[0], rest are random
    shares = []

    # Horner's polynomial evaluation method
    for x in xs:
        y = 0
        for c in reversed(coeffs):
            y = addp(mulp(y, x), c)
        shares.append(y)
    return shares



# ------------------------------------------------------------------
# Lagrange interpolation at 0
# ------------------------------------------------------------------
def reconstruct_at_zero(points: List[Tuple[int, int]]) -> int:
    xs = [x for x, _ in points]
    ys = [y for _, y in points]

    k = len(points)
    secret = 0

    for i in range(k):
        xi, yi = xs[i], ys[i]
        num, den = 1, 1
        for j in range(k):
            if i == j:
                continue
            xj = xs[j]
            num = mulp(num, (-xj))
            den = mulp(den, subp(xi, xj))
        li0 = mulp(num, pow(den, P - 2, P))
        secret = addp(secret, mulp(yi, li0))
    return secret



# ------------------------------------------------------------------
# DN07 Lagrange weights
# ------------------------------------------------------------------
def lagrange_coeffs_at_zero(xs: List[int]) -> List[int]:
    lambdas = []
    for i, xi in enumerate(xs):
        num, den = 1, 1
        for j, xj in enumerate(xs):
            if i == j:
                continue
            num = mulp(num, (-xj))
            den = mulp(den, subp(xi, xj))
        lambdas.append(mulp(num, pow(den, P - 2, P)))
    return lambdas



# ------------------------------------------------------------------
# Example 1: Addition
# ------------------------------------------------------------------

# NOTE: gather all your print statements under an 
# if verbose:
# condition. Makes our lifes easier in the next task

def example_addition(x, y, verbose: bool=False):
    n, t = 5, 2
    xs = xs_range(n)

    # input shares
    # TODO.

    # add shares
    # TODO

    # final output
    # TODO
    


# ------------------------------------------------------------------
# Example 2: 2PC Beaver Multiplication
# ------------------------------------------------------------------

# NOTE: gather all your print statements under an 
# if verbose:
# condition. Makes our lifes easier in the next task

def example_beaver(x, y, verbose: bool=False):
    n, t = 2, 1
    xs = xs_range(n)

    # input shares
    # TODO

    # Beaver triple - gen random values
    # TODO

    # Beaver triple shares
    # TODO

    # local d = x-a, e = y-b
    # TODO

    # shares of d, e
    # TODO

    # reconstruct d = x-a, e = y-b
    # TODO

    # z-sharing
    # TODO

    # final output
    # TODO



# ------------------------------------------------------------------
# Example 3: DN07 Multiplication
# ------------------------------------------------------------------

# NOTE: gather all your print statements under an 
# if verbose:
# condition. Makes our lifes easier in the next task

def example_dn07(x, y, verbose: bool=False):
    n, t = 5, 2
    xs = xs_range(n)

    # randomness required in DN07 definition
    r = gen_random_num(1, P)

    # input shares
    # TODO

    # degree t and double t shares of r
    # TODO

    # compute local h_i = share_x * share_y (degree 2t)
    # TODO

    # compute masked value [u]_{2t} = [h]_{2t} - [r]_{2t}
    # TODO

    # reconstruct u = x*y - r
    # TODO

    # produce t-shares of [z] = u + [r]_{t} = [x*y]
    # TODO
    
    # reconstruct xy
    # TODO



if __name__ == "__main__":
    example_addition(10, 5, True)
    example_beaver(10, 5, True)
    example_dn07(10, 5, True)