import compute1s

f = open("data.csv", "w")

data = [0, 1]

for x in range(2, 10**7 + 1):
    data.append(data[x-1] + compute1s.get1sDecimal(x))

for x in range(len(data)):
    f.write(f"{x},{data[x]}\n")

f.close()

# Question: Why are there repeating slopes in the graph of the data?