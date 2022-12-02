from time import sleep
import json
import os


class CalCalculator:
    def __init__(self):
        """initializing attributes"""
        # General information about AMR and BMR
        self.info = """
          BMR: 
          Your BMR is determined by your sex,
        age, and body size, and calculating
        this number tells you how about how
        many calories you burn just being 
        alive and awake
          AMR:
          Active metabolic rate (AMR), is
        calculated by multiplying your 
        BMR by an assigned number 
        representing the various activity levels.
        """

        # This is the information about how to use test results
        self.post_test_info = """
        You can use this information to help you figure out how many calories you should be
        consuming to maintain your weight. On active days, you'll need more calories, so it's 
        okay to eat a little more than you would on an average day. But on more sedentary days,
        you may want to reduce your calorie intake. If you want to lose weight, try to stay 
        below your calorie needs or increase your activity level. However, make sure you are 
        eating nutritious meals and not restricting your calories too much - eating too little
        or losing weight rapidly can be unhealthy and dangerous.
        """

        # Using flag for looping program
        self.program_active = True

        # The list of activity levels for calculating AMR
        self.activity_levels = [
            "Sedentary (little or no exercise)", "Lightly active (exercise 1–3 days/week)",
            "Moderately active (exercise 3–5 days/week)", "Active (exercise 6–7 days/week)",
            "Very active(hard exercise 6–7 days / week)"
        ]
        self.activity = int

        # Setting BMR and AMR value to float
        # Later on we will assign values
        self.bmr = float
        self.amr = float

        self.sex = ""
        self.age = int
        self.name = ""
        self.weight = float
        self.height = float

        #file for storing data
        self.file_name = "user_data.json"

    def run_program(self):
        """Runs program in a loop"""
        self.show_info()
        while self.program_active:
            self.get_info()
            self.bmr_calculator(sex=self.sex, age=self.age, height=self.height, weight=self.weight)
            self.amr_calculator(bmr=self.bmr)
            self.show_results()
            self.store_results()
            self.test_again()
        else:
            exit()

    def get_info(self):
        """Gets information about user"""
        # Give a little time to user for reading the description
        sleep(2.0)

        self.name = input("Name?\n>>>").title()
        self.age = int(input("Age?\n>>>"))
        self.sex = input("Sex? ('m' for male, 'w' for woman)\n>>>").lower()
        self.weight = float(input("Weight in kg?\n>>>"))
        self.height = float(input("Height in cm?\n>>>"))

    def show_info(self):
        """print general information"""
        print(self.info)

        if os.stat(self.file_name).st_size == 0:
            pass
        else:
            with open(self.file_name) as f:
                content = f.read().strip()
                user_data = json.loads(content)
            print("Here is your old data")
            for key, value in user_data.items():
                print(f"{key, value}")
            print()

    def bmr_calculator(self, sex, weight, height, age):
        """calculating bmr"""
        # It depends on sex of the user
        if sex == "w":
            self.bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

        elif sex == "m":
            self.bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)

    def amr_calculator(self, bmr):
        # get activity level
        self.activity_level()

        # AMR calculation depending on activity level
        if self.activity == 1:
            self.amr = bmr * 1.2
        elif self.activity == 2:
            self.amr = bmr * 1.357
        elif self.activity == 3:
            self.amr = bmr * 1.55
        elif self.activity == 4:
            self.amr = bmr * 1.725
        elif self.activity == 5:
            self.amr = bmr * 1.9

    def activity_level(self):
        """get information about activity level of user"""
        # printing activity levels
        for sen_num in range(len(self.activity_levels)):
            print(f"{sen_num + 1}- {self.activity_levels[sen_num]}")

        self.activity = int(input("\nHow active are you? (1-5)\n>>>"))

    def show_results(self):
        print(f"\nBMR: {self.bmr}\nAMR: {self.amr}")
        print(self.post_test_info)

    def test_again(self):
        test_again = input("\nDo you want to test again? ('y' for yes, 'n' for no)\n>>>").lower()
        if test_again == "n":
            self.program_active = False

    def store_results(self):
        user_info = {
            "name": self.name,
            "BMR": self.bmr,
            "AMR": self.amr,
            "height": self.height,
            "weight": self.weight,
        }
        with open(self.file_name, "w") as f:
            json.dump(user_info, f)


if __name__ == "__main__":
    cc = CalCalculator()
    cc.run_program()
