# This code file contains blanks that are meant to be filled in!
#
# Where you see "# TODO", it means that you should write some code 
# to implement the protocol! 
#
# -------------------------------------------------------------------------
#
# You are performing a yearly check of ICU units for the ministry of
# health. To that end, you need to aggregate and average the statistics
# provided by three hospitals about 6 patients.
#
# Due to strict regulation, the data must remain private! You decide to
# design an MPC protocol that will be run between the hospitals and which
# securely provides the aggregate data per hospital:
#
# 1. Each hospital sums their data column-wise
# 2. Produce secret shares of the sum of each column
# NOTE: this file is configured for SHAMIR
# 3. Exchange input shares
# 4. Locally add the shares to produce a share of the total sum per column
# 5. The shares are reconstructed on your side
# 6. The final average is calculate over the opened total sum value
# 
# NOTE: secure division via MPC is outside the scope of this demo 
#
# -------------------------------------------------------------------------

from math_helpers import P, column_sum
from secret_sharing_schemes.replicated import share_secret, add_replicated, reconstruct

# Each hospital has 2 patients with 3 statistics:
#   [Body temp, BloodPressure, Days in ICU]

H1 = [
    [38, 120, 2],   # patient 1
    [36, 115, 7]    # patient 2
]

H2 = [
    [35, 118, 1],
    [38, 125, 3]
]

H3 = [
    [40, 110, 16],
    [37, 108, 3]
]

NUM_PATIENTS = 6



# Pretty printing for frozenset keys
def pretty(party_dict):
    return {tuple(sorted(list(S))): v for S, v in party_dict.items()}



def demo_rss(n=3, t=2):
    print("==============================================")
    print("        RSS DEMO: Column-wise Averages")
    print("==============================================")

    hospitals = [H1, H2, H3]


    # Compute local sum per column per hospital
    # TODO

    # For each column j ∈ {0,1,2}, share each hospital's local sum
    # TODO

    # Open only the three total sums and print the average
    # NOTE: Do the division on the opened value!!
    # TODO



if __name__ == "__main__":
    demo_rss(n=3, t=2)
