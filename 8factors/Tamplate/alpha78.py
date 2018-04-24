def run_formula(dv):
    formula="((high+low+close)/3-Ts_Mean((high+low+close)/3,12))/(0.015*Ts_Mean(Abs(close-Ts_Mean((high+low+close)/3,12)),12))"
    alpha78=dv.add_formula('alpha170',formula,is_quarterly=False,add_data=True)
    return alpha78