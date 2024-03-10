import random

class father:
    def __init__(self, blood_type):
        self.alleles = blood_type.upper() # Setting the blood type to uppercase
    
    def contribute_alleles(self):
        return random.choice(self.alleles) # Randomly choose between two alleles

class mother:
    def __init__(self, blood_type):
        self.alleles = blood_type.upper()
    
    def contribute_alleles(self):
        return random.choice(self.alleles)

class child:
    def __init__(self, father, mother):
        self.alleles = father.contribute_alleles() + mother.contribute_alleles() # inheriting from father's and mother's randomly picked alleles and combined it here
        self.blood_type = self.choosing_blood_type()

    def choosing_blood_type(self): # Based on the diagram that have been given we're using it as a reference to determine the child blood type by comparing the choosen alleles
        if self.alleles.count('A') == 2 or (self.alleles.count('A') == 1 and self.alleles.count('O') == 1):
            return 'A'
        elif self.alleles.count('B') == 2 or (self.alleles.count('B') == 1 and self.alleles.count('O') == 1):
            return 'B'
        elif 'A' in self.alleles and 'B' in self.alleles:
            return 'AB'
        else:
            return 'O'
        
father_blood_type = input("Enter the father's Blood Type: ")
mother_blood_type = input("Enter the Mother's Blood Type: ")
        
father = father(father_blood_type)
mother = mother(mother_blood_type)

child = child(father, mother)

print("Child's allele: ", child.alleles)
print("Child's blood type: ", child.blood_type)

