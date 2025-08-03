while True:
    try:
         num1 = float(input("Введите первое число: "))
    except:
         print("Неккоректное число")
    
    operator = input("Введите оператор (+, -, *, /) ")

    try:
         num2 = float(input("Введите второе число: "))
    except:
         print("Неккоректно")

    if operator == "+":
         result = num1 + num2

         print(result)
    elif operator == "-":
         result = num1 - num2
         print(result)
    
    elif operator == "*":
         result = num1 * num2
         print(result)

    elif operator == "/":
         if num2 == 0:
              print("Ошибка! На ноль делить нельзя ")
         else:
            result = num1 / num2
            print(result)

    again = input("Хотите выполнить еще одну операцию? да/нет " ).lower()

    if again != "да":
         break 
