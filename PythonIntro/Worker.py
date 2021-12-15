class Worker:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s

    def get_salary(self):
        return self.salary

    def bonus(self):
        if self.salary > 35000:
            self.bonus = self.salary * 0.1
        print(self.bonus)

    def get_name(self):
        print(self.name, self.age, self.salary)


employee1 = Worker("Blu", 35, 40000)
employee1.get_salary()
employee1.get_name()
employee1.bonus()
employee2 = Worker("Bhaskar", 30, 45000)
employee2.get_salary()
employee2.get_name()
employee2.bonus()
