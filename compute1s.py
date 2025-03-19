def isValidInput(value):
    try: int(value)
    except: return False
    else: return True

def get1sDecimal(decimal):
    sum = 0
    if '1' not in str(decimal): return sum
    for c in str(decimal):
            if c == '1': sum +=1
    return sum

def main(n):
    n = int(n)
    sum = 0
    for x in range(1, n+1):
        a = str(x)
        if '1' not in str(a): continue
        for c in a:
            if c == '1': sum +=1
    return sum
    
if __name__ == '__main__':
    while True:
        n = input()
        if isValidInput(n): main()
        else: continue
    