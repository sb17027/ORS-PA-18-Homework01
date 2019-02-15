#ex03.py
def main():
    print("This program illustrates chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0*x*(1-x)
        print(x)
main()

# For the same number the results in exercise 2 and exercise 3 have big difference, almost two time larger.