#Bit by Bit: Kattis

def sett(bit, bits):
    bits[bit] = 1
    return bits

def clear(bit, bits):
    bits[bit] = 0
    return bits

def logicalOr(bit1, bit2, bits):
    if (bits[bit1] == '?' and bits[bit2] == 1) or (bits[bit1] == 1 and bits[bit2] == '?'):
        bits[bit1] = 1
    elif bits[bit1] + bits[bit2] == 0:
        bits[bit1] = 0
    else:
        bits[bit1] = 1
    return bits

def logicalAnd(bit1, bit2, bits):
    if (bits[bit1] == '?' and bits[bit2] == '?'):
        bits[bit1] = '?'
    elif(bits[bit1] == '?' and (bits[bit2] == 1 or bits[bit2] == 1)) or ((bits[bit1] == 1 or bits[bit1] == 0) and bits[bit2] == '?'):
        bits[bit1] = 0
    elif bits[bit1] + bits[bit2] == 2:
        bits[bit1] = 1
    else:
        bits[bit1] = 0
    return bits

def bitsToString(bits):
    bits = bits[::-1]
    bits = [str(j) for j in bits]
    return ''.join(bits[::-1])
    

numCommands = int(input())
while numCommands != 0:
    
    bits = ['?']*32
    
    for i in range(numCommands):
        #take in the manipulation
        entry = input().split()
        command = ''
        bit1, bit2 = 0, 0

        #break the manipulation into appropriate pieces
        #CLEAR AND SET
        if len(entry) == 2:
            command, bit1 = entry[0], int(entry[1])
        else:
            command, bit1, bit2 = entry[0], int(entry[1]), int(entry[2])

        #alter the list of bits by the appropriate method
        if command == 'SET':
            bits = sett(bit1, bitsToString(bits))
            print(entry, bits)
        elif command == 'CLEAR':
            bits = clear(bit1, bitsToString(bits))
            print(entry, bits)
        elif command == 'OR':
            bits = logicalOr(bit1, bit2, bits)
            print(entry, bitsToString(bits))
        else:
            bits = logicalAnd(bit1, bit2, bits)
            print(entry, bitsToString(bits))

    bits = bitsToString(bits)
    print(bits)
    numCommands = int(input())
            







        
            
