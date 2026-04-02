def entrance_fee(ages: list[int]) -> int:
    """
    calculate the admission fee of the amusement park
    :param ages: list of ages
    :return: total entry fee
    """
    kid, adult, senior = 5000, 10000, 7000
    total_fee = 0

    for age in ages:
        if age >= 65:
            total_fee += senior
        elif age >= 19:
            total_fee += adult
        else:
            total_fee += kid

    return total_fee