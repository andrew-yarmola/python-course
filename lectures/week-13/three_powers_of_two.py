def generate_powers() :
    return [ 2**x for x in range(3) ]

print("Global __name__ is :", __name__)

if __name__ == '__main__' :
    print(*generate_powers(), sep = '\n')
