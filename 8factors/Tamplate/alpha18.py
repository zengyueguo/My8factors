
def run_formula(dv, param = None):
    alpha18=dv.add_formula('alpha18','close/Delay(close,5)',is_quarterly=False,add_data=True)
    return alpha18
