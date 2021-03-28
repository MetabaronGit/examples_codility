def reduce_number(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + reduce_number(n / 2)
    else:
        return 1 + min(reduce_number(n - 1), reduce_number(n + 1))


def error_message(message: str) -> None:
    """Vypíše chybové hlášení."""
    print(f"\nChyba!\n{message}")


# Driver code
while True:
    try:
        number_for_reduce = int(input("Zadej číslo: "))
        if number_for_reduce in range(10):
            break
        error_message("Číslo musí být v rozmezí 0 - 10!")
    except:
        error_message("Zadávej poze celá čísla.")

print(f"počet kroků: {reduce_number(number_for_reduce)}");