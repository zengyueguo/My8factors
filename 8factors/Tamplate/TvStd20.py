def run_formula(dv):
    TvStd20=dv.add_formula('TvStd20','StdDev(turnover,20)/Pow(10,6)',is_quarterly=False,add_data=True)
    return TvStd20