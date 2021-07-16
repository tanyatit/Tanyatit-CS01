a= int(input("คะแนนเก็บ:"))
b= int(input("คะแนนสอบกลางภาค:"))
c= int(input("คะแนนสอบปลายภาค:"))
d=a+b+c
if d<50:
    print("F")
elif d<55:
    print("D")
elif d<60:
    print("D+")
elif d<65:
    print("C")
elif d<70:
    print("C+")
elif d<75:
    print("B")
elif d<80:
    print("B+")
else:
    print("A")