#!/usr/bin/env python3
# Advent of Code 2020 - Day 03

f = open("day03_input.txt","r")

# across 3, down 1
# input list is 323 lines, by 31 characters
# implying ~ 1000 across will be needed -> 33 repetitions of the input pattern

# produce the full map of trees
# traverse map and replace # with X and . with O
# traverse and count the X and O
# write the traversed map as output file optionally

tree_map = []

row = 0
for line in f:
    col = 0
    map_str = str("")
    while col < 1000:
        map_str = map_str + str(line[ col % 31 ])
        col += 1 
    
    tree_map.append(map_str)
    row += 1

# make a copy
processedTreeMap = list(tree_map)

targetCol = 1
row_idx = 0
for row in processedTreeMap:
    if row_idx == 0:
        # mark the starting point at upper left
        processedTreeMap[row_idx] = str("O") + row[targetCol:]
        # print('row[0] =           = {0}'.format(row))
        # print('row[0] + row[1:-1] = _{0}'.format(row[targetCol:]))
        # print('prow[0]            = {0}'.format(processedTreeMap[row_idx]))
        # print('row[{0}] set to 0'.format(0))
        pass

    else:
        targetCol = targetCol + 3
        targetChar = row[targetCol-1]
        # print('tmap[{0}] = {1}'.format(row_idx, row))
        # print('row[{0}] = {1}'.format(targetCol, targetChar))
        
        if targetChar == '.':
            processedTreeMap[row_idx] = row[:targetCol-1] + str("O") + row[targetCol:]
        elif targetChar == '#':
            processedTreeMap[row_idx] = row[:targetCol-1] + str("X") + row[targetCol:]
    
    row_idx += 1


row_idx = 0
tree_count = 0
while row_idx < 323:
    print('row: {0}'.format(row_idx))
    print('{0}'.format(tree_map[row_idx]))
    print('{0}'.format(processedTreeMap[row_idx]))
    if processedTreeMap[row_idx].find('X') > 0:
        print('found a tree!')
        tree_count += 1
    row_idx += 1

print('Encountered {0} trees'.format(tree_count))