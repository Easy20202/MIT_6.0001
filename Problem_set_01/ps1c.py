
def portion_to_save(total_cost, annual_salary, semi_annual_raise, months_to_save):
    """
    

    Parameters
    ----------
    total_cost : INT
        Total cost of the house.
    annual_salary : INT
        User annual salary.
    semi_annual_raise : FLOAT
        Semi anual raise in decimal.
    months_to_save : INT
        Number of saving months.

    Returns
    -------
    tuple containing saving rate and number of bisection iterations.

    """
    r = 0.04
    portion_down_payment = 0.25
    min_to_save = 0
    max_to_save = 10000
    n_iterations = 0
    down_payment = portion_down_payment * total_cost
    current_savings = 0
    while abs(current_savings - down_payment) > 100:
        to_save = (min_to_save+max_to_save)/2
        current_savings = 0
        salary = annual_salary
        n_iterations +=1
        for month in range(1,months_to_save + 1 ):
            current_savings += (salary/12)*(to_save/10000) + current_savings * r / 12
            if month%6 == 0:
                salary *= (1+semi_annual_raise) 
        
        if current_savings > down_payment:
            max_to_save = to_save
            
        if current_savings < down_payment:
            min_to_save = to_save
            
    print(current_savings)
    return (to_save/10000, n_iterations)


if __name__ == "__main__":
    total_cost = int(input("Please enter the total cost of your dream house: "))
    annual_salary = int(input("Please enter your annual salary: "))
    semi_annual_raise = float(input("Please enter the semi-annual raise, as decimal: "))
    months_to_save = int(input("Please input number of months you want to save: "))
    
    to_save, n_iterations = portion_to_save(total_cost, annual_salary, semi_annual_raise, months_to_save)
    print("Best saving rate is {} % of your salary".format(to_save * 100))
    print("Steps in bisection search: {}".format(n_iterations))

