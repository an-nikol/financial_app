def calculate_simple_interest(principal, rate, time_in_years):
    simple_interest = principal * (rate / 100) * time_in_years
    return simple_interest


def calculate_compound_interest(principal, rate, time_in_years):
    amount = principal * (pow((1 + rate / 100), time_in_years))
    CI = amount - principal
    return CI


def calculate_loan_payment(principal, rate, months):
    converted_rate = rate / 100
    amount = (converted_rate / 12) * (1 / (1 - (1 + converted_rate / 12) ** (-months))) * principal
    return amount


def calculate_future_value_of_savings(present_value, rate, number_of_periods):
    future_value = present_value * (1 + rate / 100) ** number_of_periods
    return future_value


def main():
    while True:
        # create a  menu that displays following options
        print()
        print('Main Menu:')
        print()
        print('1.Calculate Simple Interest')
        print('2.Calculate Compound Interest')
        print('3.Calculate Loan Payment')
        print('4.Calculate Future Value of Savings')
        print('5.Quit')
        print()

        # check for invalid input by the user
        while True:
            try:
                operation = int(input('Please, choose one of the following options(1/2/3/4/5): '))
                if 1 <= operation <= 5:
                    break
                continue
            except ValueError:
                print('Invalid number. Please try again.')

        if operation == 1:
            principal = int(input('Enter the principal amount: '))
            interest_rate = int(input('Enter the interest rate: '))
            time_in_years = int(input('Enter the time(in years): '))
            result = calculate_simple_interest(principal, interest_rate, time_in_years)
            print(f'The simple interest is: {result:.2f}')
        elif operation == 2:
            principal = int(input('Enter the principal amount: '))
            interest_rate = int(input('Enter the interest rate: '))
            time_in_years = int(input('Enter the time(in years): '))
            result = calculate_compound_interest(principal, interest_rate, time_in_years)
            print(f'The compound interest is: {result:.2f}')
        elif operation == 3:
            principal = int(input('Enter the loan amount: '))
            interest_rate = int(input('Enter the interest rate: '))
            time_in_months = int(input('Enter the time(in months): '))
            result = calculate_loan_payment(principal, interest_rate, time_in_months)
            print(f'The monthly loan payment is: {result:.2f}')
        elif operation == 4:
            present_value = int(input('Enter the present value: '))
            interest_rate = int(input('Enter the interest rate: '))
            number_of_periods = int(input('Enter the number of time periods: '))
            result = calculate_future_value_of_savings(present_value, interest_rate, number_of_periods)
            print(f'The future value of your savings is: {result:.2f}')
        elif operation == 5:
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
