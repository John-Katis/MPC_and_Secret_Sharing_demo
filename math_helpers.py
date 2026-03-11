# schemes/helpers.py
# Basic finite-field primitives and utilities shared by all schemes.

import random
from typing import List, Tuple

# A (big) prime field for all arithmetic 
# (38 digits)         P = (1 << 127) - 1
# (617 digits prime)  P = 14426749196946132614139474307305361669597733810467380712733189735015365536996481543347050483599260992690759346986336225858795263129752200219165547930131683205308178712766508191486813431285444510781421272572817962565575429626738129285425737619077522340778176818078833828509490580288720775124653974593501473446597867028731954726055652225719784402676780629855821919041717103962418792351695412820466343069233863934794563060372181343102868587686383457581546552863688391727007526109388629858357361546144503789551178288692610319706065795298236102211923801234391449199461833081526221243136308501716278176136436076581665053589

P = (1 << 127) - 1

rng = random.Random(20260310)



def modp(x: int) -> int:
    return x % P



def addp(a: int, b: int) -> int:
    return (a + b) % P



def subp(a: int, b: int) -> int:
    return (a - b) % P



def mulp(a: int, b: int) -> int:
    return (a * b) % P



def invp(a: int) -> int:
    # Fermat's little theorem: a^(P-2) mod P
    if a % P == 0:
        raise ZeroDivisionError("Attempted inverse of zero in field")
    return pow(a, P - 2, P)



def gen_random_num(start: int=0, end: int=P) -> int:
    return rng.randrange(start, end)



def gen_random_list(start, end, threshold):
    return [rng.randrange(start, end) for _ in range(threshold)]



def column_sum(matrix, col_idx):
    return sum(row[col_idx] for row in matrix) % P
