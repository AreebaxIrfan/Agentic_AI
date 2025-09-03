def main():
	# Prompt the user for the lengths of each side
	side1: float = float(input("What is the length of side 1? "))
	side2: float = float(input("What is the length of side 2? "))
	side3: float = float(input("What is the length of side 3? "))

	# Calculate the perimeter
	perimeter = side1 + side2 + side3

	# Display the result using f-string for cleaner output
	print(f"The perimeter of the triangle is {perimeter}")
	choice = input("Do you want to convert another triangle perimeter? (yes/no): ").strip().lower()
	if choice != "":
		side1: float = float(input("What is the length of side 1? "))
		side2: float = float(input("What is the length of side 2? "))
		side3: float = float(input("What is the length of side 3? "))	
		print("Thank you for using the triangle perimeter! ❄️🔥")
		return
if __name__ == '__main__':
	main()