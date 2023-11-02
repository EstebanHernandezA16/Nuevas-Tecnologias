import pandas as pd

def llenarDataF():
    print('llenando informacion')
    data = {'Nombre': ['Juan','Esteban','Alec'],
            'Edad': [25,30,15]}
    df = pd.DataFrame(data)
    print(df)

if __name__ == '__main__':
    llenarDataF()
