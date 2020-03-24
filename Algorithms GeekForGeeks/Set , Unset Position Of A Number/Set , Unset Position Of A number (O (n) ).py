def SetPosition(num):
    bit=pow(2 ,int(input("Enter Bit Position"))-1)
    try:
        if((num & bit)==bit):
            print("SET")
        else:
            print("UNSET")
    except:
        print("Bit position cant be less than equal to zero")
for _ in range(50):
    SetPosition(int(input("Enter number")))
