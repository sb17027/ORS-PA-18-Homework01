# ex07.py

def main():
    print("This program illustrates the chaootic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 3: "))
    for i in range(15):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print(x,y)
main()