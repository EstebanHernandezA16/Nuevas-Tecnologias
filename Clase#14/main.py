import pandas as pd

def llenarAlumnos():
    # print('llenando informacion')
    data = {'Nombre': ['Juan','Esteban','Alec'],
            'Edad': [25,30,15]}
    df = pd.DataFrame(data)
    print(df)


def cargarArchivo():
    data = pd.read_csv('Bd.csv')

   # print(data)
    print(data.head(5))


if __name__ == '__main__':
    cargarArchivo()
