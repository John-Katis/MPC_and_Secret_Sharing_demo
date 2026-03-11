# NOTE In this file all the code is given
# ---------------------------------------

import sys
from pathlib import Path

# Add parent directory (one level up) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from typing import Dict, List, Iterable, Tuple
from itertools import combinations
from math_helpers import P, modp, addp, subp, mulp, gen_random_num
import time



# ------------------------------------------------------------
# Utility: generate all t-subsets of {1..n}
# this defines which set of parties will hold which share
# ------------------------------------------------------------
def all_t_subsets(n, t):
    return [frozenset(s) for s in combinations(range(1, n+1), t)]



def share_secret(x, n, t) -> List[Dict[frozenset,int]]:
    subsets = all_t_subsets(n, t)
    m = len(subsets)

    base = {}

    # Pick random values for all but last subset
    total = 0
    for S in subsets[:-1]:
        r = gen_random_num()
        base[S] = modp(r)
        total = addp(total, r)


    # Final subset ensures sum == x
    last_S = subsets[-1]
    base[last_S] = modp(subp(x, total))


    # Distribute shares: party i gets all S with i ∉ S
    shares = [dict() for _ in range(n)]
    for S, val in base.items():
        for i in range(1, n+1):
            if i not in S:
                shares[i-1][S] = val

    return shares



def add_replicated(Sx, Sy):
    if len(Sx) != len(Sy):
        raise ValueError("Mismatched number of parties")

    n = len(Sx)
    out = []

    # iterate over all given shares
    for i in range(n):
        # Set of parties that hold same share
        keys_x = Sx[i].keys()
        keys_y = Sy[i].keys()

        if set(keys_x) != set(keys_y):
            raise ValueError(f"Party {i+1} subset mismatch")

        # adding pairwise (x1+y1), (x2+y2), (x3+y3)
        merged = {}
        for S in keys_x:
            # S is the subset of parties that hold the same share
            # and is used as a dictionary key
            merged[S] = addp(Sx[i][S], Sy[i][S])
        out.append(merged)

    return out



def sub_replicated(Sx, Sy):
    # Similar with add_replicated functionality

    if len(Sx) != len(Sy):
        raise ValueError("Party count mismatch in sub_replicated")

    out = []
    for i in range(len(Sx)):
        keys_x = set(Sx[i].keys())
        keys_y = set(Sy[i].keys())
        if keys_x != keys_y:
            raise ValueError("Subset mismatch in sub_replicated")
        out.append({ S: subp(Sx[i][S], Sy[i][S]) for S in keys_x })
    return out



def reconstruct(shares: Iterable[Dict[frozenset,int]], n, t, verbose: bool=False) -> int:
    needed = set(all_t_subsets(n, t))
    total_needed = len(needed)

    combined = {}
    used_shares = 0

    # check share consistency
    for idx, ps in enumerate(shares, start=1):
        used_shares += 1
        for S, v in ps.items():
            if S in combined and combined[S] != v:
                raise ValueError(f"Inconsistent duplicate share in subset {S}")
            combined[S] = v

    # how many subsets we have
    have = len(combined)
    # how many subsets are missing
    missing_subsets = needed - set(combined.keys())
    missing = len(missing_subsets)

    if verbose:
        print(f"\n--- Reconstruction Report ---")
        print(f" Parties provided       : {used_shares}")
        print(f" Total subsets needed   : {total_needed}")
        print(f" Subsets provided       : {have}")
        print(f" Subsets missing        : {missing}")
        if missing:
            print(f" Missing subsets: {sorted([list(m) for m in missing_subsets])}")

    if have < t:
        raise ValueError("Not enough shares to reconstruct")

    # sum shares
    total = 0
    for v in combined.values():
        total = addp(total, v)

    if verbose:
        print(f" Reconstructed value     : {total}")
        print(f"-------------------------------\n")

    return total



def mul_replicated(Sx, Sy, n, t):
    """
    Beaver-based multiplication for (n,t)-replicated secret sharing.
    Returns an RSS sharing of x*y.
    """

    # 1. Generate random Beaver triple (a,b,c=a*b)
    a = gen_random_num()
    b = gen_random_num()
    c = mulp(a, b)

    Sa = share_secret(a, n, t)
    Sb = share_secret(b, n, t)
    Sc = share_secret(c, n, t)

    # 2. Compute Dx = x - a   and   Dy = y - b
    Dx = sub_replicated(Sx, Sa)
    Dy = sub_replicated(Sy, Sb)

    # 3. OPEN d = x - a   and   e = y - b
    d = reconstruct(Dx, n, t, verbose=True)
    e = reconstruct(Dy, n, t, verbose=True)

    # 4. Compute z = c + d*b + e*a + d*e
    #    All done in cleartext
    z_val = c
    z_val = addp(z_val, mulp(d, b))
    z_val = addp(z_val, mulp(e, a))
    z_val = addp(z_val, mulp(d, e))

    # 5. Re-share the result as valid RSS
    Sz = share_secret(z_val, n, t)
    return Sz



def demo_addition(x, y, n, t, verbose: bool=False) -> None:
    # Share input values
    Sx = share_secret(x, n, t)
    Sy = share_secret(y, n, t)

    # Local addition
    Sz = add_replicated(Sx, Sy)

    # final output
    parties_needed = t + 1
    selected = Sz[:parties_needed]

    reconstructed = reconstruct(selected, n, t, verbose=True)

    #check
    expected = addp(x, y)
    

    assert reconstructed == expected, "Addition reconstruction failed!"

    if verbose:
        print("==== Replicated Secret Sharing: Addition Demo ====")
        print(f"Modulus P = {P}")
        print(f"Secrets: x={x}, y={y}")
        print(f"(n={n}, t={t})\n")
        # ------------------------
        print("Shares of x:")
        for i in range(n):
            print(f" P{i+1}: {Sx[i]}")
        print()

        print("Shares of y:")
        for i in range(n):
            print(f" P{i+1}: {Sy[i]}")
        print()
        # ------------------------
        print("Local addition (each party adds subset-shares component-wise):")
        for i in range(n):
            print(f" P{i+1}: {Sz[i]}")
        print()
        # ------------------------
        print("Attempting reconstruction of x+y using t+1 parties:")
        print(f"Expected = {expected}\n")
        print(f"Reconstructed = {reconstructed}\n")
        if reconstructed == expected:
            print("Correct: reconstructed x+y matches expected.\n")



def demo_mul(x, y, n, t, verbose: bool=False) -> None:
    # Share values
    Sx = share_secret(x, n, t)
    Sy = share_secret(y, n, t)

    # Do Beaver multiplication
    Sz = mul_replicated(Sx, Sy, n, t)

    # final output
    needed = t + 1
    reconstructed = reconstruct(Sz[:needed], n, t, verbose=True)

    # check
    expected = mulp(x, y)

    assert reconstructed == expected

    if verbose:
        print("==== Replicated Secret Sharing: Beaver Multiplication Demo ====")
        print(f"Modulus P = {P}")
        print(f"Secrets: x={x}, y={y}")
        print(f"(n={n}, t={t})\n")
        # ------------------------
        print("Shares of x:")
        for i in range(n):
            print(f" P{i+1}: {Sx[i]}")
        print()

        print("Shares of y:")
        for i in range(n):
            print(f" P{i+1}: {Sy[i]}")
        print()
        # ------------------------
        print("Final replicated shares of z = x*y:")
        for i in range(n):
            print(f" P{i+1}: {Sz[i]}")
        print()
        # ------------------------
        print("Reconstructing x*y using t+1 parties:")
        print(f"Expected = {expected}")
        print(f"Result = {reconstructed}")
        if expected == reconstructed:
            print("Correct: reconstructed x*y matches expected.\n")



# USE CASES
if __name__ == "__main__":
    ## ## -------------------------------------------
    demo_addition(x=10, y=5, n=3, t=2, verbose=True)


    ## ## -------------------------------------------
    # demo_mul(x=10, y=5, n=3, t=2, verbose=True)
