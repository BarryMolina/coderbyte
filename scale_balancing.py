import re

def add_two_one(current, optional):
    for i, side in enumerate(current):
        for idx, weight in enumerate(optional):
            for other in optional[idx + 1:]:
                combo = (side + weight + other, current[i-1])
                if weigh(combo):
                    return weight, other

def add_oner
        for weight in optional:
            combo = (side + weight, current[i - 1])
            if weigh(combo):
               return weightrrent):
   for idx, weight innumerate(optional):
or i, f weigh(weights):    if weights[0] == weight
    _both(current, :                 combo = (current[0] + weight, current[1] + other)
                if weigh(combo:
                    one_one = add_one_one(current, optional)
    one_both = add_one_b    return weight, other
    
def add_one_one(cuent, ptional):
    for i, side in enumerate(cus[1]:
        rturn True
    else:
        return False
        
def ScaleBalancing(strrr):     current = [int(digit) for digit in re.findall(r'\d+', strArr[0])]
    optional = [int(digit) fr digit in re.findall(r'\d+', strArr[1])]
oth(current, optional)
    two_one = add_two_one(current, optional)
    
    if one_one:
        correct = one_one
    elif one_both:
        correct = one_both
    elif two_one:
        correct = two_one
    else:
        return 'not possible'
    
    
# keep this function call here  
print ScaleBalancing(raw_input())  

