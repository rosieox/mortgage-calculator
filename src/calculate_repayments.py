import argparse

parser = argparse.ArgumentParser(description="Parameters for the mortgage calculation")
parser.add_argument("--house_val", 
                type=float, 
                dest='house_val',
                help="What value house are you trying to buy?", default=450000)

parser.add_argument("--deposit", 
                type=float, 
                dest='deposit',
                help="How much can you afford for the deposit?", default=100000)

parser.add_argument("--loan_length", 
                type=int, 
                dest='length_of_loan',
                help="How long a mortgage are you happy with (years)?", default=25)

parser.add_argument("--interest_rate", 
                type=float, 
                dest='annual_interest',
                help="What interest rate do you anticipate?", default=0.05)

args, unknown = parser.parse_known_args()

def get_monthly_mortgage_payment(house_val = 450000,
                                deposit = 100000,
                                length_of_loan = 25,
                                annual_interest = 0.05):
    
    principal = house_val - deposit
    
    length_of_loan_months = length_of_loan*12
    
    monthly_interest = annual_interest / 12
    
    interest_exp = (1+monthly_interest)**length_of_loan_months
    
    numerator = monthly_interest * interest_exp
    
    denom = interest_exp - 1
    
    monthly_repayment = principal * (numerator / denom)
    
    return monthly_repayment

def main():
    monthly = get_monthly_mortgage_payment(house_val = args.house_val,
                                deposit = args.deposit,
                                length_of_loan = args.length_of_loan,
                                annual_interest = args.annual_interest)
    
    total_repayments = monthly * args.length_of_loan * 12

    print(f'For a house valued at £{args.house_val}, annual interest rate of {args.annual_interest}%, mortgage term of {args.length_of_loan} years, and deposit of £{args.deposit},  your monthly payment will be £{monthly}. You will pay £{total_repayments} in total.')

if __name__ == "__main__":
    main()