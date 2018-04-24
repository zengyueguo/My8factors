def run_formula(dv):
    
    numerator="close-Ts_Sum(Min(low,Delay(close,1)),%s)"
    denominator="Ts_Sum(Max(high,Delay(close,1))-Min(low,Delay(close,1)),%s)"
    
    formula="({}/{}+{}/{}+{}/{})*100/(6*12+6*24+12*24)".format(
            numerator%(6),denominator%(6),
            numerator%(12),denominator%(12),
            numerator%(24),denominator%(24)
            )
    alpha159=dv.add_formula('alpha159',formula,is_quarterly=False,add_data=True)
    return alpha159
