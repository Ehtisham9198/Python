'''
Write a function that takes two set as input and returns true if one set is the subset of other else false
use this function two check if a list of sets forms a chain of subsets;
'''

def is_subset(set1, set2):
    return set1.issubset(set2) 

def forms_chain_of_subsets(sets):
    for i in range(len(sets) - 1):
        if not is_subset(sets[i], sets[i + 1]):
            return False
    return True


set1 = {1,2,3,4}
set2 = {5,6}
sets = [{1,2,3,4},{5,6}]
print("set2 is the subset of set1? ",is_subset(set2,set1))
print("Is chain of subsets? ",forms_chain_of_subsets(sets))
