def goal(input):
    input = list(str(input))

    for i in range(len(input)-1, 0, -1):
        if input[i] > input[i-1]:
            for j in range(len(input)-1, i-1, -1):
                if input[j] > input[i-1]:
                    input[i-1], input[j] = input[j], input[i-1]
                    break
            input[i:] = sorted(input[i:])
            return int("".join(input))
    return -1

def main():
    N = int(input())
    result = goal(N)
    print(result)

main()