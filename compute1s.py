def isValidInput(value):
    try: int(value)
    except: return False
    else: return True

def main(n):
    n = int(n)
    sum = 0
    for x in range(1, n+1):
        a = str(x)
        for c in a:
            if c == '1': sum +=1
    return sum
    
if __name__ == '__main__':
    while True:
        n = input()
        if isValidInput(n): main()
        else: continue
    