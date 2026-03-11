# This code file contains blanks that are meant to be filled in!
#
# Where you see "# TODO", it means that you should write some code 
# to implement the protocol! 
#
# ---------------------------------------------------------------------------
#
# You are a cybersecurity analyst and want to calculate the sum of all
# incidents across 4 secure infrastructure providers.
#
# To enable privacy, you design an MPC protocol for addition in which:
#
# 1. Providers make shares of their inputs
# 2. Providers exchange shares of input among them
# 3. Providers calculate the local share of the sum
# 4. The final shares are send to you for reconstruction
# 
# NOTE: all computations can be done locally
# NOTE: make sure to arrange the shares in the correct way for computations
#  
# ---------------------------------------------------------------------------


from math_helpers import P
from secret_sharing_schemes.replicated import share_secret, add_replicated, reconstruct
# NOTE: you can swap for Shamir

# Vendor incident counts
Palo_Alto = 10
IBM = 190
Cisco = 50
CrowdStrike = 120

incident_list = [Palo_Alto, IBM, Cisco, CrowdStrike]
vendor_names = ["Palo Alto", "IBM", "Cisco", "CrowdStrike"]



# Pretty printing for frozenset keys
def pretty(party_dict):
    return {tuple(sorted(list(S))): v for S, v in party_dict.items()}



def total_incidents(n=4, t=2):
    # Share each vendor's incident count using RSS
    # TODO

    # Add all vendors' shares locally
    # TODO

    # Reconstruct total using any t+1 = 3 parties (e.g., parties 1,2,3)
    # TODO

    opened_total = "You define it"
    return opened_total



if __name__ == "__main__":
    total = total_incidents(n=4, t=2)