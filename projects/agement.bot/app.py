def main():
	while True:
		print("What's your favorite animal?", end=" ")
		favorite_animal = input()
		print(f"My favorite animal is also {favorite_animal}!")

		# Ask if the user wants to continue
		choice = input("Do you want to enter another animal? (yes/no): ").strip().lower()
		if choice != "yes":
			print("Thank you for using the program. Goodbye!")
			break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
	main()
