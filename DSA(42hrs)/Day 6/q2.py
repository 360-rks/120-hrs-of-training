"""Softsytems Ltd is a private firm that provides software
 solutions to its customers.40 min
The management wants to calculate salary for the employees. There are two types of employees namely graduate 
who are in probation period and laterals who are experienced joiners in the company. 
Write a python program based on the class diagram given below.

RULES TO FOLLOW
===================
Class Description:
Employee class:
validate_basic_salary(): Basic salary of an employee is always more than 3000
If basic salary is valid, return true. Else return false
validate_qualification(): Employee should posses either a "Bachelors" or "Masters" degree
If qualification is valid, return true. Else return false
Graduate class:
validate_job_band(): graduate can be in "A", "B" or "C" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF+ TPI amount + incentive
    PF is 12% of basic salary
    Identify TPI amount based on cgpa
    Identify incentive based on job band. Incentive should be applied on basic
    salary (Refer tables given)
Return gross salary
Else return -1
Job Band	A	B	C	D	E	F
Incentive %	4	6	10	13	16	20

CGPA	4 to 4.25	4.26 to 4.5	4.51 to 4.75	4.76 to 5
TPI Amount	1000	1700	3200	5000
Lateral class:
validate_job_band(): Laterals can be in "D", "E" or "F" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF + SME bonus + incentive
    PF is 12% of basic salary
    Identify SME bonus based on skill set
    Identify incentive based on job band. Incentive should be applied on basic salary (Refer
    tables given)
Return gross salary
Skill Set	SME Bonus
AGP	6500
AGPT	8200
AGDEV	11500
Else return -1
Perform case sensitive string comparison.
For testing:
Create objects of Graduate and Lateral classes
Invoke calculate_gross_salary() on Graduate and Lateral objects
Display the details"""






class employee:
    def __init__(self,basic_salary,degree):
        self.basic_salary=basic_salary
        self.degree=degree

    def validate_basic_salary(self):
        if self.basic_salary>3000:
            return True
        else:
            return False
    
    def validate_qualification(self):
        if self.degree=="Bachelors" or self.degree=="Masters":
            return True
        else:
            return False
    def get_details(self):
        return [self.basic_salary,self.degree]

class graduate(employee):
    def __init__(self,basic_salary,degree,band,cgpa):
        super().__init__(basic_salary,degree)
        self.band=band
        self.cgpa=cgpa

    def validate_job_band(self):
        if self.band=="A" or self.band=="B" or self.band=="C":
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if super().validate_basic_salary() and super().validate_qualification() and self.validate_job_band():
            tpi=0
            if self.cgpa>=4 and self.cgpa<= 4.25:
                tpi=1000
            elif self.cgpa>=4.26 and self.cgpa<= 4.5:
                tpi=1700
            elif self.cgpa>=4.51 and self.cgpa<= 4.75:
                tpi=3200
            elif self.cgpa>=4.76 and self.cgpa<= 5:
                tpi=5000
            else:
                return -1
            incentive=0
            if self.band=="A":
                incentive=0.04
            elif self.band=="B":
                incentive=0.06
            elif self.band=="C":
                incentive=0.10
            gross_salary=self.basic_salary+0.12*self.basic_salary+tpi+incentive*self.basic_salary
            return gross_salary
    def get_details(self):
        temp= super().get_details()
        return temp+[self.band,self.cgpa]

class lateral(employee):
    def __init__(self,basic_salary,degree,band,skillSet):
        super().__init__(basic_salary,degree)
        self.band=band
        self.skillSet=skillSet
    def validate_job_band(self):
        if self.band=="D" or self.band=="E" or self.band=="F":
            return True
        else:
            return False
    def calculate_gross_salary(self):
        if super().validate_basic_salary() and super().validate_qualification() and self.validate_job_band():
            sme=0
            if self.skillSet=="AGP":
                sme=6500
            elif self.skillSet=="AGPT":
                sme=8200
            elif self.skillSet=="AGDEV":
                sme=11500
            else:
                return -1
            incentive=0
            if self.band=="D":
                incentive=0.13
            elif self.band=="E":
                incentive=0.16
            elif self.band=="F":
                incentive=0.20
            gross_salary=self.basic_salary+0.12*self.basic_salary+sme+incentive*self.basic_salary
            return gross_salary
    def get_details(self):
        temp= super().get_details()
        return temp+[self.band,self.skillSet]





g1=graduate(9999,"Bachelors","A",4.44)
print(g1.calculate_gross_salary())
print(g1.get_details())

l1=lateral(20000,"Masters","F","AGDEV")
print(l1.calculate_gross_salary())
print(l1.get_details())