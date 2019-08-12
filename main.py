# get and set currency pair and validation with library
first_currency_pair = input("First currency pair?")  # need to validate
second_currency_pair = input("Second currency pair?")  # need to validate
currency_pair = (first_currency_pair, second_currency_pair)

i = 0
var_list = []
run_main_loop = True


def input_var(var_msg):
    return "{0:.2f}".format(float(input(var_msg)))


def get_var(var_str):
    global run_main_loop
    yes_no = input("Do you want to add {0}? y/n".format(var_str))
    if yes_no == 'y':
        l1 = input_var("L1: ")  # get L1 value
        l2 = input_var("L2: ")  # get L2 value
        resistance_pair = (l1, l2)
        var_list.append(resistance_pair)  # set L1, L2 tuple and append to var_list
        print("{0} added to list".format(resistance_pair))
    else:
        run_main_loop = False


while run_main_loop:
    if i == 0:  # high resistance
        get_var("a high resistance")
        i += 1
    elif i == 1:  # med resistance
        get_var("a medium resistance")
        i += 1
    elif i == 2:  # support
        get_var("a support")
        i += 1
    else:  # additional variables
        get_var("another variable")
print("Your currency pair is {0}".format(currency_pair))
print("Your list of variables are {0}".format(var_list))
