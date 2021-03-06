from Goods import Goods

water_bottle = Goods(100, 10, "water bottle")
orange_juice_bottle = Goods(120, 10, "orange juice bottle")
lime_juice_bottle = Goods(110, 10, "lime juice bottle")


def show_goods():
    print('Please select item...')
    print('1. Water : ' + str(water_bottle.get_price()) + ' ks')
    print('2. Orange Juice : ' + str(orange_juice_bottle.get_price()) + ' ks')
    print('3. Lime Juice : ' + str(lime_juice_bottle.get_price()) + ' ks')
    print('q. Quit')


def sell_goods():
    cart = []
    end = False

    while not end:

        show_goods()
        input_type = input('What would you like to buy? Please choose 1 or 2 or 3 or q')

        if input_type == '1':
            count_bottle(cart, input_type, water_bottle)

        elif input_type == '2':
            count_bottle(cart, input_type, orange_juice_bottle)

        elif input_type == '3':
            count_bottle(cart, input_type, lime_juice_bottle)

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


def count_bottle(cart, input_type, good):
    try:
        input_amount = int(input('How many number would you like to buy?'))
        check_result = check_stock(input_type, input_amount)
        if check_result:
            cart.append(good.multiply_temp_price(input_amount))
            good.reduce_amount(input_amount)
        else:
            print('Out of stock for ' + good.name + ".")
    except ValueError:
        print('Invalid data inputting. Please type a number.')


def check_stock(input_type, amount):
    if input_type == '1':
        return water_bottle.compare_amount(amount)

    elif input_type == '2':
        return orange_juice_bottle.compare_amount(amount)

    elif input_type == '3':
        return lime_juice_bottle.compare_amount(amount)


def calculate_cost(item_list):
    total_cost = 0
    for item in item_list:
        total_cost += item
    return total_cost


def main():
    sell_goods()


if __name__ == '__main__':
    main()
