
def months_needed_for_downpayment(total_cost, annual_salary, portion_saved, semi_annual_raise):
    """
    Parameters
    ----------
    total_cost : INT
        Total cost of your dream house.
    annual_salary : INT
        Your annual salary.
    portion_saved : FLOAT
        Portion of salary you expect to save (0.1 = 10%).
    semi_annual_raise: FLOAT
        Decimal percentage of semi-annual salary raise. (Occurs every 6th, 12th, 18th month and so on...)

    Returns
    -------
    n_months : INT
        Number of months needed to save for the downpayment, downpayment = 25% of total_cost

    """
    portion_down_payment =  0.25
    #r = annual return 0.04 = 4%
    r = 0.04
    current_savings = 0
    n_months = 0 
    
    down_payment = total_cost * portion_down_payment
    
    while current_savings < (down_payment-100):
        n_months +=1
        current_savings += (annual_salary/12)*portion_saved + current_savings * r / 12
    
        if n_months%6 == 0:
            annual_salary *= (1+semi_annual_raise) 
    print(current_savings)
    return n_months


if __name__ == "__main__":
    total_cost = int(input("Please enter the total cost of your dream house: "))
    annual_salary = int(input("Please enter your annual salary: "))
    portion_saved = float(input("Please enter the portion you want to save, as decimal: "))
    semi_annual_raise = float(input("Please enter the semi-annual raise, as decimal: "))

    
    
    n_months = months_needed_for_downpayment(total_cost, annual_salary, portion_saved, semi_annual_raise )
    print("You need {} months to save for the downpayment".format(n_months))
    