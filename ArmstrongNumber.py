def isArmstrongNumber(number_to_check):
    number_list = str(number_to_check)
    summary = 0
    for number in number_list:
        summary += int(number)**len(number_list)
    return(number_to_check == summary)
