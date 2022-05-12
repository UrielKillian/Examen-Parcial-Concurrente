# Help Functions

def ValAbs(x, y):
    if x > y:
        return x - y
    else:
        return y - x

# -----------------------------


def queens(solution, state, n):
    if state >= n:
        return False
    result = False
    while True:
        if (solution[state] < n):
            solution[state] = solution[state] + 1
        if (validate(solution, state)):
            if state != n-1:
                result = queens(solution, state+1, n)
                if result == False:
                    solution[state+1] = 0
            else:
                print(solution)
                for x in range(n):
                    for i in range(n):
                        if solution[x] == i+1:
                            print("X"),
                        else:
                            print("- "),
                    print("\n")
                result = True
        if (solution[state] == n or result == True):
            break
    return result


def validate(solution, state):
    for i in range(state):
        if(solution[i] == solution[state]) or (ValAbs(solution[i], solution[state]) == ValAbs(i, state)):
            return False
    return True


print("Type The Numbers Of Queens:\n")
n = input()
solution = []
for i in range(n):
    solution.append(0)
state = 0
print(queens(solution, state, n))
