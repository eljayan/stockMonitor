import pandas, mypaths


def load (path):
    df = pandas.read_excel(mypaths.SAVEPATH, sheet_name=None, header=8, index_col = 0, usecols="B:I", parse_dates=True)
    
    #elimina las filas que no contienen valores completos en la fila, como las ultimas que solo tienen texto
    df18 = df["2018"].dropna(axis=0, how="any") 
    df19 = df["2019"].dropna(axis=0, how="any")
    master = df18.append(df19)

    #convertir el lindice a fecha
    master.index = pandas.to_datetime(master.index)
    
    return master


def company_select(company_name):
    
    return company = master.loc[master["EMISOR"]==company_name, :]



def ohlc(df):
    return df["PRECIO"].resample("D").ohlc()


if __name__ == '__main__':
    d = load(mypaths.SAVEPATH)
    print d.describe()
