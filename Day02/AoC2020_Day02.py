#!/usr/bin/env python3
# Advent of Code 2020 - Day 02

f = open("day02_input.txt","r")

valid_count = 0

for line in f:
    valid = False
    colon = line.find(':')
    policy = line[0:colon]
    # print(policy)
    hyphen = policy.find('-')
    space = policy.find(' ')
    pol_min = int(policy[0 : hyphen])
    pol_max = int(policy[hyphen + 1 : space])
    pol_char = policy[-1]
    pw = line[colon+2:-1]

    char_count = pw.count(pol_char)
    if char_count >= pol_min and char_count <= pol_max:
        valid = True
        valid_count += 1

        print('VALID {0} - {1} {2} : {3}    {4}'.format(pol_min, pol_max, pol_char, pw, char_count))
    else:
        print('FAIL {0} - {1} {2} : {3}    {4}'.format(pol_min, pol_max, pol_char, pw, char_count))

print('Total valid = {0}'.format(valid_count))