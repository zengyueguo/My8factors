def run_formula(dv):
    Increment=dv.add_formula('Increment','If(volume<Delay(volume,1),(close-Delay(close,1))/close,0)',is_quarterly=False)
    temp=Increment
    temp.iloc[0,:]+=100
    temp[(temp.isnull().shift(1)&temp.notnull()).fillna(False)]+=100
    NVI=temp.cumsum()
    dv.append(NVI,'NVI')
    return NVI