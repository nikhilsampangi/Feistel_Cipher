import random


def toBinary(ip):
    if ip > 1:
        return int(str(toBinary(ip//2)) + str(ip % 2))
    return ip


def arrToBinary(ip):
    # ip_bin=[]
    # for x in ip:
    #   temp=toBinary(x)
    #   ip
    ip_bin = [toBinary(x) for x in ip]
    # print(ip_bin)
    # converting ascii values to 7 bit binary format
    for x in range(len(ip_bin)):
        ip_bin[x] = "0"*(7-len(str(ip_bin[x]))) + str(ip_bin[x])
    # print(ip_bin)
    return ip_bin


def strToASCII(ip):
    ip_asc = [ord(x) for x in ip]
    return ip_asc


def strToBin(ip):
    asc = strToASCII(ip)
    print(asc)
    return arrToBinary(asc)


def generateKey(size):
    key = ""
    for i in range(size):
        key = key+str(random.randint(0, 1))
    return key


def bitwiseXor(ip1, ip2):
    if(len(ip1) > len(ip2)):
        ip1, ip2 = ip2, ip1  # swapping
    prefix = len(ip2)-len(ip1)
    ip1 = "0"*prefix+ip1
    # print(ip1)
    # print(ip2)
    result = ""
    for i in range(len(ip2)):
        if(ip1[i] == ip2[i]):
            result += "0"
        else:
            result += "1"
    return result


def binToDec(ip):
    tmp = 0
    op = 0
    for i in range(len(ip)):
        op += (2**tmp)*int(ip[-(i+1)])
        tmp += 1
    return op


def binToStr(ip):
    op = ""
    for i in range(0, len(ip), 7):
        temp = ip[i:i+7]
        op += chr(binToDec(temp))
        # print(temp)
        # print(binToDec(temp))
        # print(chr(binToDec(temp)))
    # print(op)
    return op


def feistelAlgo(L1, R1, K1, K2):
    # Round - 1
    F1 = bitwiseXor(R1, K1)
    R2 = bitwiseXor(F1, L1)
    L2 = R1
    # Round - 2
    F2 = bitwiseXor(R2, K2)
    R3 = bitwiseXor(L2, F2)
    L3 = R2
    return L3, R3


def feistel(pln_txt):

    decr = strToBin(pln_txt)
    # print(decr)
    mid = len(decr)//2
    L1 = decr[:mid]
    R1 = decr[mid::]
    L1 = "".join(L1)
    R1 = "".join(R1)
    # print(L1)
    # print(R1)
    K1 = generateKey(len(R1))
    K2 = generateKey(len(R1))
    # print(K1)
    # print(K2)
    L3, R3 = feistelAlgo(L1, R1, K1, K2)
    # ciphertext
    encr_txt = binToStr(L3+R3)
    print("encrypted text is : ", encr_txt)
    # decryption
    L1, R1 = feistelAlgo(L3, R3, K1, K2)
    decr_text = binToStr(L1+R1)
    print("decrypted text is: ", decr_text)


if __name__ == '__main__':
    # ip = bytearray(input("Enter message to encrypt:"), "utf-8")
    pln_txt = str("originalmsg")
    encr = feistel(pln_txt)
    # print(ToBinary(13))
