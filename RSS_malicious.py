# This code file contains blanks that are meant to be filled in!
#
# Where you see "# TODO", it means that you should write some code 
# to implement the protocol! 
#
# -------------------------------------------------------------------------
#
# In this scenario, 4 parties receive shares of a value `secret`
# and reconstruct that value.
# BUT, there is a malicious party that tampers with one of the shares.
# The reconstrcution fails and the parties want to find the cheater.
#
# Your task is to write an `audit` function that, once reconstrcution has
# failed, will identify the cheater. Instructions are given below.
#
# NOTE: it is impossible in this simple scenario to identify the single
# NOTE: cheater. You will have to find a pair of parties instead.
# NOTE: One of them is guaranteed to be the cheater.
#
# -------------------------------------------------------------------------

from math_helpers import addp
from secret_sharing_schemes.replicated import share_secret, reconstruct

# Pretty print helper
def pretty(d):
    return {tuple(sorted(list(S))): v for S, v in d.items()}



def audit_subset_mismatches_and_pairs(shares, n=4, t=2):
    """
    For each t-subset S, two parties hold the same subset-share.
    If the holders disagree → mismatch + cheating pair printed.
    """
    print("\n=========== SUBSET CONSISTENCY AUDIT ===========")

    # Setting: in audit mode, we have all shares - this could the dealer for example
    # The process is:

    # TODO
    # 1. Make a list of share index and value - 
    # - since out scheme is (4,2), each share index should have 2 values

    # TODO
    # 2. Check each share index and the values
    # If the values are the same there was no tampering
    # If the values differ, there was tampering
    
    mismatches = ["you", "define", "this"]
    return mismatches



def demo_tamper():
    n, t = 4, 2
    secret = 42

    # Dealer shares the secret
    shares = share_secret(secret, n, t)

    print("============== INITIAL SHARES (HONEST) ==============")
    for i in range(n):
        print(f"Party {i+1}: {pretty(shares[i])}")

    print("\n============== PARTY 3 TAMPERS ==============")
    cheater = 2  # Party 3 (0-based)
    S = next(iter(shares[cheater].keys()))
    old = shares[cheater][S]
    shares[cheater][S] = addp(old, 777)   # corrupt by +777

    print(f"Party 3 changed subset {tuple(sorted(list(S)))} "
          f"from {old} to {shares[cheater][S]}")

    print("\n============== SHARES AFTER TAMPERING ==============")
    for i in range(n):
        print(f"Party {i+1}: {pretty(shares[i])}")

    # Reconstruction
    print("\n============== RECONSTRUCTION AFTER TAMPER ==============")
    try:
        val = reconstruct(shares, n, t, verbose=False)
        print(f"Reconstructed value = {val}")
    except Exception as e:
        print("Reconstruction ERROR:", e)

    # Audit
    audit_subset_mismatches_and_pairs(shares, n, t)



if __name__ == "__main__":
    demo_tamper()
