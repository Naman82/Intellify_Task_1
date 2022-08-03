# function which returns frequency dictionary
def give_remainder_dict(dividend, divisor, num_digits_after_dec:int):
    quotient = round(dividend / divisor, num_digits_after_dec)
    # declaration of frequency dictionary
    freq_dict = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }
    # if the number of digits after decimal input is zero by user it directly returns quotient and frequency dictionary
    if(num_digits_after_dec == 0):
        return quotient, freq_dict
    flag_dec = 0
    # iterating through the quotient to count the number of digits after decimal
    for ch in str(quotient):

        if(flag_dec == 0):
            if(ch != '.'):
                continue
            flag_dec = 1
            continue
        if ch in freq_dict.keys():
            freq_dict[ch] += 1
            continue
        freq_dict[ch] = 1
    
    return quotient, freq_dict

    

def main():
    # taking input from the user 
    dividend = int(input("Enter dividend : "))
    divisor = int(input("Enter divisor : "))
    digits_num = int(input("Enter number of digits after decimal : "))

    # printing the answer 
    print(give_remainder_dict(dividend,divisor,digits_num))


# calling main function 
main()
