from random import randint
import requests
from datetime import datetime, timedelta
class rare:
    rare = ''
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.id = self.get_id()
        self.hp = randint(100,200)
        self.power = randint(10,20)

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.id = self.get_id()
        self.last_feed_time = datetime.now()
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']["front_shiny"])
        else:
            return "https://avatars.mds.yandex.net/i?id=9bd5af2367af0c45d7efc5c932d55d5288f258d5-5494327-images-thumbs&n=13"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_id(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['id'])
        else:
            return "id"
        
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chanse = randint(1,5)
            if chanse == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\nID покемона {self.id}\nЗдоровье {self.hp}\nСила покемона {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"
        
class Wizard(Pokemon):
    def feed(self):
        return super().feed(hp_increase=20)

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.сила -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    def feed(self):
        return super().feed(feed_interval=10)