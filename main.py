from finance import Account


owner = input("Введите имя владельца счета: ")

account = Account(owner)


while True:
    print("\nФинансовый сервис")
    print("1. Пополнить счет")
    print("2. Списать средства")
    print("3. Показать баланс")
    print("4. Показать историю операций")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        amount = float(
            input("Введите сумму пополнения: ")
        )

        account.deposit(amount)

        print("Счет успешно пополнен.")

    elif choice == "2":
        amount = float(
            input("Введите сумму списания: ")
        )

        if account.withdraw(amount):
            print("Средства успешно списаны.")
        else:
            print("Недостаточно средств.")

    elif choice == "3":
        print(
            "Текущий баланс:",
            account.show_balance(),
            "руб."
        )

    elif choice == "4":
        transactions = account.show_transactions()

        if len(transactions) == 0:
            print("История операций пуста.")
        else:
            print("\nИстория операций:")

            for transaction in transactions:
                print(transaction)

    elif choice == "0":
        print("Работа программы завершена.")
        break

    else:
        print("Неизвестная команда.")
