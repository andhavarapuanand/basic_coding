temp=input("Enter a number: ")
fact=1
while True:
    try:
        if int(temp)>=0:
            for num in range(int(temp)):
                fact*=(num+1)
            print(f"{temp} ! = {fact}")
            break
        else:
            print("Error: enter +ve intergers only !")
            temp=input("Enter a number: ")
    except:
        print("Error: enter +ve intergers only !")
        temp=input("Enter a number: ")