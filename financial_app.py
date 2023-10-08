def calculate_simple_interest(principal, rate, time_in_years):
    simple_interest = principal * (rate / 100) * time_in_years
    return simple_interest


def calculate_compound_interest(principal, rate, time_in_years):
    amount = principal * (pow((1 + rate / 100), time_in_years))
    CI = amount - principal
    return CI


def calculate_loan_payment(principal, rate, months):
    amount = (rate / 12) * (1 / (1 - (1 + (rate / 12) / 100) ** (-months))) * principal
    return amount


def calculate_future_value_of_savings(present_value, rate, number_of_periods):
    future_value = present_value * (1 + rate / 100) ** number_of_periods
    return future_value


def main():
    while True:
        # create a  menu that displays following options
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
            print(f'The simple interest is: {result}')
        elif operation == 2:
            pass
        elif operation == 3:
            pass
        elif operation == 4:
            pass
        elif operation == 5:
            pass
        



principall = float(input())
ratee = float(input())
moths = int(input())

print(calculate_future_value_of_savings(principall, ratee, moths))
