
users = [
    {
        'login': 'Egor',
        'password': 'Letov',
        'img': 'https://uznayvse.ru/person/egor-letov/egor_letov04.jpg',
        'isAdmin': False
    },
    {
        'login': 'Yura',
        'password': 'Hoy',
        'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlXLkEpHNd1HPAuvYHgC_blnaBvGCThmnyCFEG_4e3dv68I2Y4Ah2buxfFZuoKy-OKhoM&usqp=CAU',
        'isAdmin': False
    },
    {
        'login': 'admin',
        'password': 'zhiv',
        'img': 'https://persons.life/wp-content/uploads/2021/01/viktor-coy-400x400.jpg',
        'isAdmin': True
    }
]

alboms = [
    {
        'name': 'Всё идёт по плану',
        'author': 'Гражданская оборона',
        'genre': 'Rock',
        'img': 'https://upload.wikimedia.org/wikipedia/ru/b/ba/%D0%92%D1%81%D1%91_%D0%B8%D0%B4%D0%B5%D1%82_%D0%BF%D0%BE_%D0%BF%D0%BB%D0%B0%D0%BD%D1%83_%28%D0%B0%D0%BB%D1%8C%D0%B1%D0%BE%D0%BC%2C_1988%29.jpg',
     
        'about': 'Для настоящих бунтарей!',
        'comments': [
            {
                'user': users[0],
                'comment': "Панки Хой!",
                'raiting': 10
            },
        ],

    },
    {
    
        'name': 'Просвистела',
        'genre': 'Rock',
        'author': 'ДДТ',
        'img': 'https://upload.wikimedia.org/wikipedia/ru/f/f8/DDT-Prosvistela.jpg',
        'about': 'Для любителей наполненого инструментала..',
        'comments': [
            {
                'user': users[1],
                'comment': "Переслушиваю третий раз!",
                'raiting': 8
            }
        ],

    },
    {
        'name': 'Heaven & Hell',
        'genre': 'POP',
        'author': 'Ava Max',
        'img': 'https://upload.wikimedia.org/wikipedia/ru/6/6c/Ava_Max_%E2%80%94_Heaven_%26_Hell.jpg',
        'about': 'Про человеческую натуру',
        'comments': [
            {
                'user': users[2],
                'comment': "Попса, но хороша!",
                'raiting': 10
            }
        ],

        
    },
    {
        'name': 'Money for Nothing',
        'genre': 'Classic Rock',
        'author': 'Dire Straits',
        'img': 'https://upload.wikimedia.org/wikipedia/en/d/dd/Moneyfornothing2.jpg',
        'about': 'Золотая классика',
        'comments': [
            {
                'user': users[0],
                'comment': "Марк удивляет!",
                'raiting': 9
            }
        ],

        
    },
]

genre = 'All'
genres = ['All']

for albom in alboms:
    if not genres.__contains__(albom['genre']):
        genres.append(albom['genre'])
    
    if albom['comments'] and len(albom['comments']) > 0:
        middle = 0
        for comment in albom['comments']:
            middle += int(comment['raiting'])
    
    albom['raiting'] = int(middle/len(albom['comments']))

isLogin = False
isAdmin = False

user = None

def GetalbomByName(name: str):
    for albom in alboms:
        if(albom['name'] == name):
            return albom
    return None

def CheckRaiting():
    for rest in alboms:
        if rest['comments'] and len(rest['comments']) > 0:
            middle = 0
            for comment in rest['comments']:
                middle += int(comment['raiting'])
    
        rest['raiting'] = int(middle/len(rest['comments']))

def CheckGeners():
    genres.clear()
    genres.append('All')
    for albom in alboms:
        if not genres.__contains__(albom['genre']):
            genres.append(albom['genre'])

