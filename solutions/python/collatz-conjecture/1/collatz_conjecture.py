def steps(number):
    if(number > 0):
        total_number_of_steps = 0
        while(number > 1):
            if(number % 2 == 0):
                number = number/2
                total_number_of_steps += 1
            else:
                number = (number * 3) + 1
                total_number_of_steps += 1
        return total_number_of_steps
    else:
       raise ValueError("Only positive integers are allowed") 
