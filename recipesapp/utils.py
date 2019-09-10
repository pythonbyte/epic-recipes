from decimal import Decimal


def convert_unit(cost, ri_amount, i_amount, ri_unit, i_unit):
    if ri_unit == i_unit:
        return Decimal(ri_amount / i_amount) * cost

    elif ri_unit == "G" and i_unit == "KG":
        converted_i_amount = i_amount * 1000
        return Decimal(ri_amount / converted_i_amount) * cost

    elif ri_unit == "KG" and i_unit == "G":
        converted_ri_amount = ri_amount * 1000
        return Decimal(ri_amount / converted_ri_amount) * cost

    elif ri_unit == "L" and i_unit == "CL":
        converted_ri_amount = ri_amount * 10
        return Decimal(ri_amount / converted_ri_amount) * cost

    elif ri_unit == "CL" and i_unit == "L":
        converted_i_amount = i_amount * 10
        return Decimal(ri_amount / converted_i_amount) * cost
