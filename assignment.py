#Add a constructor for the class cohort
#Create a method / function to the class that prints the cohort name and the total number of students.
#create a new instance of the cohort class.
class Cohort:
    def _init_(self,cohort_name,student_name,reg_no,total_students):
        self.cohort_name=cohort_name
        self.student_name=student_name
        self.reg_no=reg_no
        self.total_students=total_students
    def print_cohort_info(self):
        print(f"Cohort name:{self.cohort_name}")
        print(f"The student name is {self.student_name}")
        print(f"The student's Registration number is :{self.reg_no}")
        print(f"Total number of students:{self.total_students}")

#create a new instance of the cohort class1.   
cohort1=Cohort("Cohort 4",58)

#Call the method to print cohort details
cohort1.print_cohort_info()
 