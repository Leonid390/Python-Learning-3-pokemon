from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.hp = randint(12, 24)
        self.power = randint(3, 6)

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        #self.navik = self.get_ability_name()
        
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"

    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

# метод атаки
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            if randint(1, 5) == 4:
                return('Shielded')
        
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return (f'Сражение с @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n\n'
                    f'Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}') 
        else:
            enemy.hp = 0
            return f'Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}'





    #def get_type(self):
     #   url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
      #  response = requests.get(url)
       # if response.status_code == 200:
        #    data = response.json()
         #   return (data['types']['slot'][1]['type']['name'])
        #else:
         #   return "Pikachu"

    #def get_ability_name(self):
     #   url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
      #  response = requests.get(url)
       # if response.status_code == 200:
        #    data = response.json()
         #   return (data['abilities'][0]['ability']['name'])
    # Метод класса для получения информации
    def info(self):
        return (f"Имя твоего покеомона: {self.name}\n"
                f"Здоровье твоего покеомона: {self.hp}\n"
                f"Сила твоего покеомона: {self.power}")
    #def skill(self):
     #   return f"Навыки твоего покеомона: {self.navik}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        powerfull = randint(2, 6)
        self.power += powerfull
        результат = super().attack(enemy)
        self.power -= powerfull
        return результат + f"\nБоец применил супер-атаку силой:{powerfull} "

