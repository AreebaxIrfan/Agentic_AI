def main():
    # Define ages with clear variable names and type annotations
    anton: int = 21
    beth: int = anton + 6
    chen: int = beth + 20
    drew: int = chen + anton
    ethan: int = chen  # Ethan has the same age as Chen

    # Display the results with proper formatting
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")


# Required to run the main function
if __name__ == '__main__':
    main()
