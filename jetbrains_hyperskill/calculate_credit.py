from math import log, ceil, floor
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type", type=str, required=False, choices=["annuity", "diff"], help=""
    )
    parser.add_argument("--payment", type=int, required=False, help="")
    parser.add_argument("--principal", type=int, required=False, help="")
    parser.add_argument("--periods", type=int, required=False, help="")
    parser.add_argument("--interest", type=int, required=False, help="")
    return parser.parse_args()


def validate_args(arguments):
    if not arguments.type or arguments.type not in ["diff", "annuity"]:
        print("Incorrect parameters")
        exit()
    if arguments.type == "diff" and arguments.payment:
        print("Incorrect parameters")
        exit()
    if not arguments.principal and not arguments.payment:
        print("Incorrect parameters")
        exit()
    if not arguments.simple_interest:
        print("Incorrect parameters")
        exit()


def calculate_count_of_months(p, a, i):
    n = log((a / (a - i * p)), 1 + i)
    return ceil(n)


def print_count_of_months(n):
    years = n // 12
    months = n % 12
    if years == 0:
        print("You need", months, "months to repay this credit!")
    elif months == 0:
        print("You need", years, "years to repay this credit!")
    else:
        print("You need", years, "years and", months, "months to repay this credit!")


def calculate_monthly_payment(p, n, i):
    a = p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    return ceil(a)


def calculate_principal(a, n, i):
    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    return floor(p)


def calculate_diff_payment(p, n, i):
    d = 0
    for m in range(1, n + 1):
        dm = ceil(p / n + i * (p - (p * (m - 1)) / n))
        print("Month " + str(m) + ": paid out " + str(dm))
        d += dm
    return d


def calculate(arguments):
    overpayment = 0
    i = float(arguments.simple_interest) / (12 * 100)
    if arguments.type == "annuity":
        if not arguments.payment:
            periods = int(arguments.periods)
            principal = int(arguments.principal)
            m_payment = calculate_monthly_payment(principal, periods, i)
            print("Your annuity payment = " + str(m_payment) + "!")
        elif not arguments.principal:
            periods = int(arguments.periods)
            m_payment = float(arguments.payment)
            principal = calculate_principal(m_payment, periods, i)
            print("Your credit principal = " + str(principal) + "!")
        elif not arguments.periods:
            principal = int(arguments.principal)
            m_payment = float(arguments.payment)
            periods = calculate_count_of_months(principal, m_payment, i)
            print_count_of_months(periods)
        overpayment = m_payment * periods - principal
    elif arguments.type == "diff":
        principal = int(arguments.principal)
        periods = int(arguments.periods)
        d = calculate_diff_payment(principal, periods, i)
        overpayment = d - principal
    print("Overpayment =", int(overpayment))


args = get_args()
validate_args(args)
calculate(args)
