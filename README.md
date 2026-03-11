# Demo of MPC and Secret Sharing

This repo contains 6 files that are relevant for demonstations and the `math_helpers` one. There are 2 demonstrations related to secret sharing and 4 related to MPC protocols.

All the demonstrations can be run within their files.

## DIY

5 out of 6 demonstrations are filled with TODOs instead of code. The idea is to apply what has been discussed in class about these protocols and implement them yourselves!

## Secret Sharing

There are 2 schemes implemented here:

1. RSS - fully implemented

Implements a (1) simple addition protocol and (2) replicated multiplication.

2. SSS - DIY

You will have to implement a (1) addition, (2) 2 party multiplication and (3) n-party multiplication.

### MPC

Note that for all following scenarios, the "parties" are "in the head". This means that no infrastructure for communicating parties is provided.

Instead, you should assume the existence of parties and think carefully about share distribution and other operations, such that you get the correct result.

#### Scenario 1: Cybersecurity Incidents

In file `cybersecurity_incidents.py`, you want to add the cybersecurity incidents from 4 secure network providers in a privacy-preserving way.

In the file, a description of an MPC protocol is provided. Your task is to implement it using either Shamir or Replicated secret sharing.

#### Scenario 2: Malicious RSS Share Auditing

In file `RSS_malicious`, a function is given, in which parties receive shares of a secret value, exchange, and open them.

On of the parties has tampered with the shares. This is detected due to the structure of the existing code. Your task is to write an additional function that takes the tampered shares and outputs a potential cheating pair.

#### Scenario 3: Healthcare Statistics

In files `hospitals_with_RSS.py` and `hospitals_with_SSS.py`, some hospital data are given. Your task is to implement an MPC protocol that correctly aggragates the total sum of the hospital data column-wise and reveals only the total sum. Based on this, you can get the average statistics for 6 patients.

Each file provides the different imports needed to implement the protocol using different secret sharing schemes.
