import random

pas = input("Enter new password: ")
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    # "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Volkswagen, das Auto": {"fuel": 300, "strength": 9999999, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}


class Sim:
    def __init__(self, name="Human", car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = True
        self.car = car
        self.home = False
        self.check = ""
        self.fake_pas = True
        self.job = random.choice(list(job_list))
        self.salary = 40  # job_list[self.job]["salary"]
        self.gladness_less = 23  # job_list[self.job]["gladness_less"]
        self.alive = True

    def get_home(self):
        if self.alive == True:
            self.money -= 2000
            print("You have a home!")
            self.home = True

    def get_car(self):
        pass

    def chill(self):
        if self.alive == True:
            self.gladness += 17
            self.money -= 3
            print(f"Gladness is {self.gladness}")
            if self.home == True:
                self.gladness += 5

    def log(self):
        self.check = input("Enter ur password: ")
        if self.check == pas:
            pass
        else:
            print("U stupid niga! Fuck of this account now mzfk!")
            self.fake_pas = False

    # def get_job(self):
    # luck = random.randint(1, 4)
    # if luck == 1:
    # self.job = "Python developer"
    # elif luck == 2:
    # self.job = "Java developer"
    # elif luck == 3:
    # self.job = "C++ developer"


class Auto(Sim):
    def __init__(self, brand_list):
        super().__init__()
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class Job(Sim):
    def work(self):
        if self.alive == True:
            self.money += self.salary
            self.gladness -= self.gladness_less
            print(f"{self.money} money but {self.gladness} gladness")
        else:
            pass

    def less_work(self):
        if self.gladness <= -300:
            if self.alive == True:
                self.job = False
                if self.home == True:
                    print("You loosed a job and jumped from the roof! But you had a pretty house!")
                else:
                    print("You loosed a job and jumped from the roof!")
                self.alive = False
        else:
            pass


Human = Job()
Human.log()
if Human.fake_pas == True:
    while Human:
        luck = random.randint(1, 3)
        if luck == 1:
            Human.work()
        elif luck == 2:
            Human.chill()
        if Human.money >= 2000:
            Human.get_home()
        Human.less_work()