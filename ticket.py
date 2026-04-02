def entrance_fee(ages: list[int]) -> int:
    """
    Calculate the total admission fee for an amusement park based on ages.

    :param ages: list[int] - list of visitor ages
    :return: int - total admission fee

    Rules:
    - Age < 3: free
    - Age 3~12: 5000
    - Age 13~64: 10000
    - Age 65+: 7000
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