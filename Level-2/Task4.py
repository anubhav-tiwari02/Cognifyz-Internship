def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        print("\n================================")
        print("       TEMPERATURE CONVERTER")
        print("================================")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))

                if celsius < -273.15:
                    print("Invalid temperature! Below absolute zero.")
                    continue

                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"\n{celsius:.2f}°C = {fahrenheit:.2f}°F")

            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == "2":
            try:
                fahrenheit = float(
                    input("Enter temperature in Fahrenheit: ")
                )

                if fahrenheit < -459.67:
                    print("Invalid temperature! Below absolute zero.")
                    continue

                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"\n{fahrenheit:.2f}°F = {celsius:.2f}°C")

            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == "3":
            print("\nThank you for using Temperature Converter!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
