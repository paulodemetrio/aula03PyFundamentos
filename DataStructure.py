if __name__ == "__main__" :
    # Criando dicionário
    d1 = {}   # Vazio
    d1 = dict()

    d2 = {'Curso':'Python', 'Sala':'Blue'}   # Preenchido
    d2 = dict(curso='Python', sala='Blue')

    print(d1,d2)

    user = {
        'id': 10,
        'score': 7.5,
        'tipo': ['readator'],
        'info':{
            'nome': 'José',
            'setor': 14,
            'nível': 2 
        },
        'ativo': True
    }

    print(user)
    print('---'*10)
    print(user['info'])
    for ch in user:
        print(ch)
    print(f'Retornando keys(): {user.keys()}')
    print(f'Retornando values(): {user.values()}')
    print(f'Retornando items(): {user.items()}')

    for vl in user.values():
        print(vl)
    
    for ch, vl in user.items():
        print(f'{ch}: {vl}')

    user['score'] = 8.0
    print(user['score'])

    user['cidade'] = 'Indaial'
    print(user['cidade'])

    user.update({'cidade' : 'Blumenau', 'ativo' : False})
    print(user)