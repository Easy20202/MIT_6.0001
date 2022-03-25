
def months_needed_for_downpayment(total_cost, annual_salary, portion_saved):
    """
    Parameters
    ----------
    total_cost : INT
        Total cost of your dream house.
    annual_salary : INT
        Your annual salary.
    portion_saved : FLOAT
        Portion of salary you expect to save (0.1 = 10%).

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
    
    while current_savings < down_payment:
        n_months +=1
        current_savings += (annual_salary/12)*portion_saved + current_savings * r / 12
    
    return n_months



if __name__ == "__main__":
    total_cost = int(input("Please enter the total cost of your dream house: "))
    annual_salary = int(input("Please enter your annual salary: "))
    portion_saved = float(input("Please enter portion you want to save per month, as decimal: "))
    
    n_months = months_needed_for_downpayment(total_cost, annual_salary, portion_saved)
    print("You need {} months to save for the downpayment".format(n_months))
