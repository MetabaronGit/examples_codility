def solution(S: str) -> int:
    """
    Vrací počet kroků potřebných k snížení zadaného čísla na 0.

    :param n: zadané číslo v binárním tvaru
    :return: počet potřebných kroků
    """
    counter = 0
    try:
        value = int(S, 2)
    except:
        print("Number must be in binary form!")
    finally:
        if len(S) > 1000000:
            print("Number is out of range!")
        else:
            while value > 0:
                counter += 1

                if value % 2 == 0:
                    value //= 2
                else:
                    value -= 1

    return counter


if __name__ == "__main__":

    S = 400 * "1"
    # S = "011100"
    print(f"počet kroků: {solution(S)}")
