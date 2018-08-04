waterPri = 100
waterNoOfBottle = 10;

orangeJuicePri = 120
orangeNoOfBottle = 10;

limeJuicePri = 110
limeNoOfBottle = 10;


def show_goods():
    print('Please select item...')
    print('1. Water : ' + str(waterPri) + ' ks')
    print('2. Orange Juice : ' + str(orangeJuicePri) + ' ks')
    print('3. Lime Juice : ' + str(limeJuicePri) + ' ks')
    print('q. Quit')


def sell_goods():
    cart = []
    end = False
    global waterNoOfBottle
    global orangeNoOfBottle
    global limeNoOfBottle
    while not end:

        show_goods()
        input_type = input('What would you like to buy? Please choose 1 0r 2 or 3 or q')

        if input_type == '1':
            input_amount = int(input('How many number would you like to buy?'))
            check_result = check_stock(input_type, input_amount)
            if check_result:
                cart.append(waterPri*input_amount)
                waterNoOfBottle -= input_amount
            else:
                print('Out of stock for water bottle.')
                break

        elif input_type == '2':
            input_amount = int(input('How many number would you like to buy?'))
            check_result = check_stock(input_type, input_amount)
            if check_result:
                cart.append(orangeJuicePri * input_amount)
                orangeNoOfBottle -= input_amount
            else:
                print('Out of stock for orange juice bottle.')
                break

        elif input_type == '3':
            input_amount = int(input('How many number would you like to buy?'))
            check_result = check_stock(input_type, input_amount)
            if check_result:
                cart.append(limeJuicePri * input_amount)
                limeNoOfBottle -= input_amount
            else:
                print('Out of stock for lime juice bottle.')
                break

        else:
            end = True

        if not end:
            decision = input('Would you like to buy again? y or n')
            if decision == 'y':
                end = False
            else:
                end = True

    if len(cart) > 0:
        print('Total : ' + str(calculate_cost(cart)))
    print('Thank you')


def check_stock(input_type, amount):
    if input_type == '1':
        if (waterNoOfBottle - amount) > -1:
            return True
        else:
            return False

    elif input_type == '2':
        if (orangeNoOfBottle - amount) > -1:
            return True
        else:
            return False

    elif input_type == '3':
        if (limeNoOfBottle - amount) > -1:
            return True
        else:
            return False


def calculate_cost(item_list):
    total_cost = 0
    for item in item_list:
        total_cost += item
    return total_cost


def main():
    sell_goods()


if __name__ == '__main__':
    main()

