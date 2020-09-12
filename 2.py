# Welcome to Daniel's python generated fibonacci sequence

startingNum = int(input("\nEnter the first letter of your fibonacci sequence = "))

howLong = int(input("-\nHow long do you want your sequence to be? = "))

fibonacci = [startingNum, startingNum + 1]

lenFib = len(fibonacci)

for i in range(lenFib + howLong):
    new = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(new)

print("-")
print(fibonacci)
