class Student:
    def __init__(self,name,age,grade):
      self.name=name
      self.age=age
      self.grade=grade

    def introduce(self):
       print(f"my name is {self.name},my age is {self.age}, my grade is {self.grade} ")

    def isPassing(self):
       if self.grade>=50:
          return "pass"

       else:
          return "fail"

student1=Student("lana",22,98)
student2=Student("sara",20,78)
student3=Student("noor",18,45)

student1.introduce()
print(student1.isPassing())

student2.introduce()
print(student2.isPassing())