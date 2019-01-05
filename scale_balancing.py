import re

def add_two_one(current, optional):
    for i, side in enumerate(current):
        for idx, weight in enumerate(optional):
            for other in optional[idx + 1:]:
                combo = (side + weight + other, current[i-1])
                if weigh(combo):
                    return weight, other

def add_one_both(current, optional):
    for idx, weight in enumerate(optional):
        for i, other in enumerate(optional):
            if i != idx:
                combo = (current[0] + weight, current[1] + other)
                if weigh(combo):
                    return weight, other
    
def add_one_one(current, optional):
    for i, side in enumerate(current):
        for weight in optional:
            combo = (side + weight, current[i - 1])
            if weigh(combo):
                return weight
    
def weigh(weights):
    if weights[0] == weights[1]:
        return True
    else:
        return False
        
def ScaleBalancing(strArr): 
    current = [int(digit) for digit in re.findall(r'\d+', strArr[0])]
    optional = [int(digit) for digit in re.findall(r'\d+', strArr[1])]

    one_one = add_one_one(current, optional)
    one_both = add_one_both(current, optional)
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

