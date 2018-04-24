def run_formula(dv):
    rstr12=dv.add_formula('rstr','Ts_Sum(Log(close_adj/Delay(close_adj,1)),240)',is_quarterly=False,add_data=True)
    return rstr12
