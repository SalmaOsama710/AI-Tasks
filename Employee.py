Salary=5000
Age=25
JobTitle="computer science"
JobBouns=500

def GetBouns(Money):
    if(Salary>Money):
        Money+=500
        print(Money)

def CheckCareer(Title):
    if(Title==JobTitle):
        print("correct")

def CheckAge(age):
    if(age>=Age):
        print("Enter The Interview")