

def run_formula(dv, param = None):
    Decay_linear_content1="((high+low)/2+high)-(vwap+high)"
    Decay_linear_content2="Correlation(((high+low)/2),Ts_Mean(volume,40),3)"
    
    Rank1="Rank(Decay_linear({},20))".format(Decay_linear_content1)
    Rank2="Rank(Decay_linear({},6))".format(Decay_linear_content2)
    
    alpha77=dv.add_formula('alpha77','Min({},{})'.format(Rank1,Rank2),is_quarterly=False,add_data=True)
    
    return alpha77
