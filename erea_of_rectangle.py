x=0
print("what type do rectangle you want double-dimensional or three-dimensional")
while(x != 3 and x != 2):
        x=int(input("put 2 or 3 "))
if(x==2):
    length = float(input("input the lenght of the rectangle: "))
    whith = float(input("input the whith of the rectangle: "))
    erea = length * whith
    print(f"the erea of the rectangle = {erea} ^2")
else :
    length = float(input("input the lenght of the rectangle: "))
    whith = float(input("input the whith of the rectangle: "))
    height = float(input("input the height of the rectangle: "))
    erea = length * whith * height
    print(f"the erea of the rectangle = {erea} ^3")



