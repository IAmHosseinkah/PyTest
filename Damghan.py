n = int(input())

bomb = 2
virus = n
counter = 1

while True:
    if virus - bomb < 2:
        print(counter)
        break
    bomb += 2
    virus += 1
    counter += 1
