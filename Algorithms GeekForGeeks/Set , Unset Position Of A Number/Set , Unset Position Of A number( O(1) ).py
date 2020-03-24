def SetPosition(num):
    bit=int(input("Enter Bit Position"))
    try:
        print("SET")if (num>>(bit-1)&1) else print("UNSET")
    except ValueError:
        print("Please Enter  valid Bit less than or equal to zero is not valid!")
        
for _ in range(50):
    SetPosition(int(input("Enter number")))
