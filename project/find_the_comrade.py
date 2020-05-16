'''
Program to complete se sequence of all polymers found in a given file
Example:
$python find_the_comrade.py list10000polyg_N400_seq0001_be0.400_3d_ooo.dat
Hence all polymers in list10000polyg_N400_seq0001_be0.400_3d_ooo.dat are
competed and saved in the list "polymers" (see the code for more details)
'''
import sys
import numpy as np
from collections import Counter

path_dat = sys.argv[1] # path to file with the polymers
path_ent = path_dat.replace('ooo.dat','hhh.dat.ent') # path to the info about type of node

# print file paths for debugging
print('Files to be open:')
print(path_dat)
print(path_ent)

#################### reading file .ent to save knotted polymers
# only polymers with a knot
poly_number = [] # list for polymer number that has a knot
knot_number = [] # compleentary list of poly_number to store which knot

with open(path_ent, mode='r') as f:
    for line in f:
        splitted = line.split()
        poly_number.append(splitted[0]) # save line number
        knot_number.append(splitted[2]) # save 3rd column, i.e. type of knot

################### reading file .dat to extrapolate sequences
# array with polymers sequences as extracted from file
polymers = []
# Converting lists into arrays
# Note: lists are more efficient of appending but arrays are faster in operations
poly_number = np.array(poly_number)
# scaling number of line from file .ent to file .dat
# NOTE: NUMBERING IN .ENT STARTS FROM 1
poly_number = (poly_number).astype('int')*4 # now this contains the line
                                            # in which there are the polymer sequences

with open(path_dat, mode='r') as f:
    for idx, line in enumerate(f):

        # selecting only the line needed
        if (idx+1) in poly_number: # idx start from 0, while numbers
                                    # in poly_number start from 1
            polymers.append(line.rstrip()) # .rstrip() remouve the final \n from line

# the choise of saving a polymer as a string is based on using the method
# Counter from collections to count the numbers in the string and fin the
# last step. NOTE: string uses twice (approx) memory respect to int but
# th above mentioned reason compensate for this disadvantage

################## Finding the last steps
for idx, poly in enumerate(polymers):
    c = Counter(poly)   # (sub class of) dict with the numbers appearing
                        # in the sequence counted
    # Idea: find the non matching numbers: 0 goes with 3 (+x and -x) and so on.
    x = c['0'] - c['3']
    y = c['1'] - c['4']
    z = c['2'] - c['5']
    # E.g. if x = +1, this means that a 3 is missing
    # Moreover, if z = -2 it means that two 2 are missing
    if x != 0:
        if x > 0:
            polymers[idx] = poly + '3'*x
        else:
            polymers[idx] = poly + '0'*abs(x)
    elif y != 0:
        if y > 0:
            polymers[idx] = poly + '4'*y
        else:
            polymers[idx] = poly + '1'*abs(y)
    elif z != 0:

        if z > 0:
            polymers[idx] = poly + '5'*z
        else:
            polymers[idx] = poly + '2'*abs(z)
            

print(f'\nNumber of polymers found in {path_dat}:\n{len(polymers)}')
