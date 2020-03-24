def bin(n):
    if (n > 1):  
        bin(n >> 1)
    print(n & 1, end = "") 
bin(int(input("ENTER NUMBER")))
