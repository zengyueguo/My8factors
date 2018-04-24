def run_formula(dv):
    formula="((((Rank((1/close))*volume)/Ts_Mean(volume,20))*((high*Rank((high-close)))/(Ts_Sum(high,5)/5)))-Rank((vwap-Delay(vwap,5))))"
    alpha170=dv.add_formula('alpha170',formula,is_quarterly=False,add_data=True)
    return alpha170