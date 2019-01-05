def increment(state):
    state[0] += 1
    for i, counter in enumerate(state):
        if counter > 3:
            state[i] = 0
            state[i + 1] += 1
    return state
    
def CorrectPath(str):
    x, y = 0, 0
    a, b = 4, 4
    path = [char for char in str]
    directions = ['r', 'd', 'l', 'u']
    questions = []
    state = []
    for i, char in enumerate(path):
        if char == '?':
            questions.append(i)
            state.append(0)
    #print state
    #print path
    #print questions
    
    while x != a and y != b:
    #for x in range(10):
        for i, question in enumerate(questions):
            # change question mark to the direction indicated by counter in state 
            path[question] = directions[state[i]]
        #print state, questions, path
        x, y = 0, 0
        for direction in path:
            if direction == 'r':
                x += 1
            elif direction == 'd':
                y += 1
            elif direction == 'l':
                x -= 1
            elif direction == 'u':
                y -= 1
            else:
                print('string parsing error')
                break
            if x < 0 or x > 4:
                break
            elif y < 0 or y > 4:
                break
        state = increment(state)
    return path
    
def follow_path(path):
    x, y = 0, 0
    for direction in path:
        if direction == 'r':
            x += 1
        elif direction == 'd':
            y += 1
        elif direction == 'l':
            x -= 1
        elif direction == 'u':
            y -= 1
        else:
            print('string parsing error')
        print x, y
# keep this function call here  
print CorrectPath(raw_input())  


  
