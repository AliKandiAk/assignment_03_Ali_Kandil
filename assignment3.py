student_data = [
    {
        "ID": 1,
        "Name": "Alice",
        "Age": 20,
        "Major": "Computer Science",
        "GPA": 3.7
    },
    {
        "ID": 2,
        "Name": "Boby",
        "Age": 21,
        "Major": "Engineering",
        "GPA": 3.9
    },
    {
        "ID": 3,
        "Name": "Bob",
        "Age": 21,
        "Major": "Engineering",
        "GPA": 3.9
    }
]

def Get_Studentby_ID(Data,id):#choice 1
    for i in Data:
        if i["ID"]==id:
            return i 
    return None

def GetStudent_byMajor(Data, major):#choice 3
    same_major = []
    for i in Data:
        if i["Major"].lower() == major.lower():
            same_major.append(i["Name"])
    return same_major

def Add_Student(Data,name,age,major,gpa):#choice 4
  id = len(Data)+1
      
  new_student = {
    "ID": id,
    "Name": name,
    "Age": age,
    "Major": major,
    "GPA": gpa}
  Data.append(new_student)

def Highest_GPA(Data):#choice 8
    highest_gpa=[]
    for i in Data:
      if i["GPA"]>3:
          highest_gpa.append(i["Name"])
    return tuple(highest_gpa)

def Remove_Student(Data, id):#choice 6
    for i in Data:
        if i["ID"] == id:
            Data.remove(i)
            return "Student has been deleted"

def Calculate_Average(Data):#choice 7
    totalgpa=0
    
    students_nb=len(Data)
    for i in Data:
        totalgpa+=i["GPA"]
    if totalgpa>0:
      avarage=totalgpa/students_nb
      return avarage
    else: 
        return None
        
    

while True:
  x=input("Enter choice number:")
  if x=="1":
      id=int(input("enter student ID:"))
      Get_Studentby_ID(student_data,id)
  elif x=="2":
      print(student_data)
  elif x=="3":
       major=input("enter student major:")
       GetStudent_byMajor(student_data,major)
  elif x=="4":
      name=input("enter your name:")
      age=int(input("enter your age:"))
      mj=input("enter your major:")
      Gpa=int(input("enter your gpa:"))
      Add_Student(student_data,name,age,mj,Gpa)
  elif x=="5":
      pass
  elif x=="6":
    id=int(input("enter student id to remove:"))
    Remove_Student(student_data,id)
  elif x=="7":
     print(Calculate_Average(student_data))
  elif x=="8":
      print("studnets with the highest Gpa are:")
      print(Highest_GPA(student_data))
  elif x=="9" :
      exit() 
      
