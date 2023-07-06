def show_request(num_of_oper: int) -> int:
    '''Вычисление операции и ее суммы'''
    if num_of_oper == 1:
        income = int(input("Insert amount of money in transaction: "))
        return income
    elif num_of_oper == 2:
        consumption = int(input("Insert amount of consuming money: "))
        return consumption


def tax(amount_of_money: int) -> int:
    '''Сумма налога за 3 операции'''
    amount_of_money *= 0.03
    return amount_of_money


def count_comission(consumption: int) -> int:
    '''Высчитывание суммы комиссии при снятии денег'''
    comission = consumption * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600
    return comission


def count_income(amount_of_money: int) -> int:
    '''Подсчет суммы зачисления на счет'''
    amount_of_money += income
    return amount_of_money


def show_money_on_acc(amount_of_money: int) -> str:
    answer = f'Money on your acc - {amount_of_money}'
    return answer


sum_on_acc = 0
counter = 0
SUPERPROFIT = 5000000

while True:
    if sum_on_acc >= SUPERPROFIT:
        sum_on_acc -= sum_on_acc * 0.1
    num_of_operation = int(input("Operation: "))
    if num_of_operation == 1:
        income = show_request(num_of_operation)
        print(f"Our account has income in size of {income}, "
              f"sum in account is {sum_on_acc}, counter on percent of remainder - {2 - counter}")
        if income % 50 == 0:
            sum_on_acc += count_income(sum_on_acc)
            counter += 1
            if counter > 2:
                sum_on_acc += tax(sum_on_acc)
                counter = 0
        else:
            print("Our value should be aliquot to 50!")
    elif num_of_operation == 2:
        consumption = show_request(num_of_operation)
        if consumption < sum_on_acc and consumption % 50 == 0:
            sum_on_acc -= (consumption + count_comission(consumption))
            counter += 1
            if counter > 2:
                sum_on_acc += tax(sum_on_acc)
                counter = 0
        else:
            print("Not enough money or not aliquot to 50 ")
    else:
        print(show_money_on_acc(sum_on_acc))
