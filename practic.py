class Student :
    def __init__(self, name , years , GPA):
        self.name = name
        self.years = years
        self.gpa = GPA
    def get_name(self):
        return self.name
    def get_years(self):
        return self.years
    def get_gpa(self):
        return self.gpa
    def set_name(self, name):
        self.name = name
    def set_years(self, years):
        self.years = years
    def set_gpa(self, gpa):
        self.gpa = gpa
    def get_all_info(self):
        print(f'Имя студента {self.name} , его возраст {self.years} , его средний балл {self.gpa}')
        
class Higher_Year_Student(Student):
    def __init__(self, name, years, GPA , title_of_thesis):
        super().__init__(name, years, GPA)
        self.title_of_thesis = title_of_thesis
    def get_name(self):
        return self.name
    def get_years(self):
        return self.years
    def get_gpa(self):
        return self.gpa
    def get_title(self):
        return self.title_of_thesis
    def set_name(self, name):
        self.name = name
    def set_years(self, years):
        self.years = years
    def set_gpa(self, gpa):
        self.gpa = gpa
    def set_title(self, title):
        self.title_of_thesis = title
    def get_all_info(self):
        print(f'Имя студента {self.name} , его возраст {self.years} , его средний балл {self.gpa}, название его проектной работы {self.title_of_thesis}')
student1 = Student("Иван",20, 4.0 )

student2 = Higher_Year_Student("Анна",22,4.5,"Исследование квантовой механики")

student1.get_all_info()
student2.get_all_info()