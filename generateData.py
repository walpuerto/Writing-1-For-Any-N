import compute1s

f = open("data.csv", "w")

print("Generating data...")

for x in range(1, 99999):
    f.write(f"{x},{compute1s.main(x)}\n")

f.close()

# Question: Why are there repeating slopes in the graph of the data?