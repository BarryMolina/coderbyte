def CorrectPath(string):
    path = [char for char in string]
    directions = ['r', 'd', 'l', 'u']
    questions = []
    state = []
    for i, char in enumerate(path):
        if char == '?':
            questions.append(i)
            state.append(0)
    state_string = []
    while True:
        matrix = [[0 for x in range(5)] for y in range(5)]
        matrix[0][0] = 1
        x, y = 0, 0
        for i, question in enumerate(questions):
            path[question] = directions[state[i]]
        for direction in path:
            if direction == 'r':
                x += 1
            elif direction == 'd':
                y += 1
            elif direction == 'l':
                x -= 1
            elif direction == 'u':
                y -= 1
            try:
                if matrix[y][x] == 1:
                    break
                matrix[y][x] = 1
            except IndexError:
                break
        if x == 4 and y == 4:
            return ''.join(path)
        state[0] += 1
        try:
            for i, counter in enumerate(state):
                if counter > 3:
                    state[i] = 0
                    state[i + 1] += 1
        except IndexError:
            break
print CorrectPath(raw_input())  
