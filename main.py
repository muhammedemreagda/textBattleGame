def calculate(arm,hl):
    temp=0
    if(arm<=25):
        temp=hl//10+(arm//10)
    elif(arm>25 and arm<=50):
        temp=hl//7+(arm//7)
    elif(arm>50 and arm<=75):
        temp=hl//4+(arm//4)
    elif(arm>75 and arm<=100):
        temp=hl//4+(arm//2)
    return hl+arm+temp

heal = int(input('Enter your heal: '))
armor = int(input('Enter your armor: '))

if(heal==0):
    print("You dead")
elif(heal>0 and armor==0):
    print(f"Your total health:{heal}")
elif(heal>0 and armor>0):
    total=calculate(armor,heal)
    print(f"Your total health:{total}")
