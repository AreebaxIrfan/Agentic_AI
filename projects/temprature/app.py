def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    while True:
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"\nTemperature: {fahrenheit}F = {celsius}C\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")
            continue

        choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thank you for using the temperature converter. Stay cozy! ❄️🔥")
            break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
