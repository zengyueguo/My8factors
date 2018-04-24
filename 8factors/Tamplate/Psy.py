def run_formula(dv,param=None):
    defult_param = {'N':12}      
    if not param:
        param = defult_param
    N = param['N']
    Psy = dv.add_formula('Psy','Ts_Sum(close_adj>Delay(close_adj,1),%s)/%s'%(N,N),is_quarterly=False,add_data=True)
    return Psy