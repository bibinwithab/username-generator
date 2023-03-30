import random
import string


class Person:
    def __init__(self, firstname, secondname, age) :
        self.firstname = firstname
        self.secondname = secondname
        self.age = age

    def email(self):
        n_1 = self.firstname.lower()
        n_2 = self.secondname.lower()
        print(f"Email: {n_1}{n_2}{self.age}{random.randint(1, 10)}@hotmail.com")

    def username(self):
        print(f"Username: {self.firstname.lower()}_{random.randint(1, 100)}")

    def password(self):
        length = 2 + len(self.firstname)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        all = lower + upper + num
        passwords = random.sample(all, length)
        password = "".join(passwords)
        print(f"Password: {password}")

    def talk(self):
        print(f"Hello {self.firstname} {self.secondname}!")
        if int(self.age) < 18:
            print("You do not fulfil the age requirement.")
        else:
            self.email()
            self.username()
            self.password()
            self.welcome()

    def welcome(self):
        print("Feel free to access our webpage using the provided username and password.")


firstname = input("First Name: ")
secondname = input("Second name: ")
age = int(input("Age: "))
name_1 = Person(firstname,secondname,age)

name_1.talk()
