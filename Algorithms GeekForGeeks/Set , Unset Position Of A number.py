def SetPosition(num):
    bit=(2 ^ int(input("Enter Bit Position"))) 
    if(num & bit==1):
        print("SET")
    else:
        print("UNSET")
   
