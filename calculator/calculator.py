# Here is the full Object-Oriented Calculator implementation using Python. 
# This calculator follows OOP principles, including encapsulation, inheritance, and method-based operations.
# It also includes exception handling to prevent errors like division by zero

# class to define the calcultor
class calculator:
    
    """ This is a simple calculator have attributes simple arithmatic operations"""
    
    # define the function for add
    def add(self,a , b):
        return a + b
    
    # define the function for substraction
    def subtract(self, a, b):
        return a - b
    
    # define the function for multiplication 
    def multiply(self, a, b):
        return a * b
    
    # define the function for division
    def divide(self, a, b):
        if b ==0:
            return "Error! Division by zero is valid"
        return a / b
    

# To add another class to define advanced calculator which additionla characteristics    
class AdvanceCalculator(calculator):
    """ Little advanced calculator to find the power """
    def power(self,a, b):
        return a ** b
    
    
# main menu of this calculator
def main():
    calc = AdvanceCalculator()
    
    print("-"*50)
    while True:
        print("\n==== Object Oriented Calculator ====")
        print("1. Add")
        print("2. substraction")
        print("3. multiplication")
        print("4. Division")
        print("5. power (a^b)")
        print("6. Exit")

        print("-"*50)
        
        choice = input("Enter the choice (1-6): ")
        
        if choice == "6":
            return "Exiting the calculator. Thank you!"
            break
        elif choice not in {'1','2','3','4','5'}:
            print("invalid choice! please enter between 1 to 6")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
        except ValueError:
            print("Invalid Input! please enter numeric value")
            continue
        
        if choice=="1":
            print(f"Result : {num1} + {num2} = {calc.add(num1,num2)}")
            
        if choice=="2":
            print(f"Result : {num1} - {num2} = {calc.subtract(num1,num2)}")
            
        if choice=="3":
            print(f"Result : {num1} × {num2} = {calc.multiply(num1,num2)}")
            
        if choice=="4":
            print(f"Result : {num1} ÷ {num2} = {calc.divide(num1,num2)}")
            
        if choice=="5":
            print(f"Result : {num1} ^ {num2} = {calc.power(num1,num2)}")
            
        print("-"*50)
        
        again = input("Do you want to perform further calculations (yes/no)").strip().lower()
        if again =="no":
            print("Thank you for using the calculator")
            break

if __name__ == "__main__":
    print(main())
    
            
    
    
        
    