class Mother:
    mothername = ""
def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""
def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Mother's Name:", self.mothername)
        print("Father's Name:", self.fathername)

# Driver's code
s1 = Son()
s1.mothername = "abc"
s1.fathername = "xyz"
s1.parents()