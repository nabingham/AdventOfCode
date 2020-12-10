#!/usr/bin/env python3
# Advent of Code 2020 - Day 02

f = open("day02_input.txt","r")

valid_count = 0

for line in f:
    posValid = 0
    colon = line.find(':')
    policy = line[0:colon]
    # print(policy)
    hyphen = policy.find('-')
    space = policy.find(' ')
    pos1 = int(policy[0 : hyphen])
    pos2 = int(policy[hyphen + 1 : space])
    pol_char = policy[-1]
    pw = line[colon+2:-1]

    print(line)
    print('{0} - {1} {2} : _{3}_({4})'.format(pos1, pos2, pol_char, pw, len(pw)))

    # NB: python is zero based, but pw policy is 1-based
    substr = pw[pos1-1 :pos1]
    print('  {0} = {1} at pos {2}'.format(substr, pol_char, pos1))
    if substr == pol_char:
        posValid += 1

    substr = pw[pos2-1:pos2]
    print('  {0} = {1} at pos {2}'.format(substr, pol_char, pos2))
    if substr == pol_char:
        posValid += 1

    if posValid == 1:
        valid_count += 1
        print('PASS\n')
        
    else:
        print('FAIL\n')

print('\n\nTotal valid = {0}'.format(valid_count))