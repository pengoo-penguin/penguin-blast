# TODO name vlt ändern, bot fertig, display fertig, loop im dpiel, mehrere modus mit merheren runden machen

from random import randint

class Penguin(object):
    MAX_HEALTH = 100
    __slots__ = ['_Penguin__strength', '_Penguin__defence', '_Penguin__aim', '_Penguin__speed', '_Penguin__healthpoints', '_Penguin__multiplier', '_Penguin__coins', '_Penguin__inventory', 'status', 'max_health', 'alive']
    
    def __init__(self):
        self.status = 'normal'

        self.__strength = 10
        self.__defence = 10
        self.__aim = 10
        self.__speed = 10
        self.__healthpoints = Penguin.MAX_HEALTH
        
        self.__multiplier = 1
        self.__coins = 0
        self.__inventory = []
        
        self.alive = True
        
    def __str__(self):
        if self.status == 'normal':
            '''
            (o_
            //\
            V_/_
            '''
            return '(o_\n//\\\nV_/_'
        elif self.status == 'dead':
            '''
            (x_
            //\
            V_/_
            '''
            return '(x_\n//\\\nV_/_'
        elif self.status == 'rich':
            '''
            ($_
            //\
            V_/_
            '''
            return '($_\n//\\\nV_/_'
        elif self.status == 'shocked':
            '''
            (O_
            //\
            V_/
            '''
            return '(O_\n//\\\nV_/_'
        elif self.status == 'slapped':
            '''
            (o|
            //\
            V_/_
            '''
            return '(o|\n//\\\nV_/_'
        elif self.status == 'smoking':
            '''
            (o_.'
            //\
            V_/_
            '''
            return '(o_.\'\n//\\  ~~\nV_/_'

        elif self.status == 'invisible':
            '''
             o
            
            
            '''
            return ' o \n\n'
        elif self.status == 'healed':
            '''
            (^_
            //\
            V_/_
            '''
            return '(^_\n//\\\nV_/_'
        elif self.status == 'bow':
            '''
            (o_ /\
            /\\< -)->
            V_/_\/
            '''
            return '(0_ /\\\n/\\\\< -)->\nV_/_\\/'
        elif self.status == 'chainsaw':
            '''
                #
            (o_ #
            //\-X 
            V_/_
            '''
            return '   #\n(o_ #\n//\\-X \nV_/_'
        elif self.status == 'gun':
            '''
            (^_
            //\.–
            V_/_
            '''
            return '(^_\n//\\.–\nV_/_'
        elif self.status == 'superman':
            '''
               (o_
             _-//$
            -  V_/_
            '''
            return '   (o_\n _-//$\n-  V_/_'
        elif self.status == 'car':
            '''
                (o_
            .---//\-..
            +(_)--(_)' 
            '''
            return '    (o_\n.---//\\-..\n+(_)--(_)\''
        elif self.status == 'medkit':
            '''
              (^_
              //\
            [+]_/_
            '''
            return '  (^_\n  //\\\n[+]_/_'
        
    
    def get_strength(self):
        return self.__strength
    def set_strength(self, upgrade):
        self.__strength+=upgrade
        
    def get_defence(self):
        return self.__defence
    def set_defence(self, upgrade):
        self.__defence+=upgrade
    
    def get_aim(self):
        return self.__aim
    def set_aim(self, upgrade):
        self.__aim+=upgrade
    
    def get_speed(self):
        return self.__speed
    def set_speed(self, upgrade):
        self.__speed+=upgrade
    
    def get_health(self):
        return self.__healthpoints
    
    def get_multiplier(self):
        return self.__multiplier
    
    def get_coins(self):
        return self.__coins
    def add_coins(self, amount):
        self.__coins += amount
    def remove_coins(self, amount):
        self.__coins -= amount
    
    def get_inventory(self):
        return self.__inventory
    def add_item(self, item):
        self.__inventory.append(item)
    def remove_item(self, item):
        if item in self.__inventory:
            self.__inventory.remove(item)
            return True
        else:
            return False

    def take_damage(self, damage):
        self.__healthpoints -= damage
        if self.__healthpoints <= 0:
            self.alive = False
            self.status = 'dead'

    def recharge(self):
        self.__multiplier += 1
        return self.__multiplier
    
    def attack(self, opponent):
        difference = self.__aim*1.5 - opponent.get_aim()
        
        if difference > 0:
            damage = self.__strength * 1.5 * self.__multiplier - opponent.get_defence()
            if self.__multiplier > 1:
                self.__multiplier = 1

            if damage > 0:
                return damage
            else:
                return 0
        else:
            return -1

    def fish_slap(self):
        return self.__strength * 0.2

    def snowball_rampage(self):
        snowballs = randint(0,100)

        if snowballs < 50:
            return 0
        else:
            damage = snowballs * 0.01
            return damage


        
class Player(Penguin):
    __slots__ = ['_Player__name']
    def __init__(self, name):
        Penguin.__init__(self)
        self.__name = name
    
    def get_name(self):
        __slots__ = ['_Bot__name']
        return self.__name
        

class Bot(Penguin):
    def __init__(self, name):
        Penguin.__init__(self)
        self.__name = name

    def get_name(self):
        return self.__name

    def choose_action(self, opponent):
        health_ratio = self.get_health() / Penguin.MAX_HEALTH


class Shop(object):
    upgrade_cost = 10 
    def __init__(self):
        self.items = {
            'Unsichtbarkeitsumhang': 10, # {'Der Pinguin wird unsichtbar und kann nicht getroffen werden!':
            'Pflaster':10, #{'Heilt 10 HP (nur einmalig nutzbar)': 
            'Pfeil & Bogen':20, #{'erhalte Pfeil und Bogen für den Rest der Runde und erziele doppelt so vielen Schaden!'
            'Kettensäge':30, #{'Erhlte eine Kettensäge für den Rest der Runde und erziele 3x so vielen Schaden!':
            'Revolver':40, #{'erhalte einen Revolver für den Rest der Runde der 4x so viel Schaden macht! (schreibe r um Russich Roulette zu spielen)':
            'Auto':50, #{'Fahre für den Rest der Runde mit einem Auto rum und erschwere deinen Gegner so, dich zu treffen!':
            'Medizinkoffer':50, #:{'Heilt den Pinguin komplett!'
            'Superman Anzug':100, #:{'Werde stärker & schneller & robuster für den ganzen Rest der Runde!'
        }
        self.upgrades = [
            'Stärke',
            'Verteidigung',
            'Zielgenauigkeit',
            'Geschwindigkeit'
        ]
    def buy(self, player, purchase_type, purchase):
        if purchase_type == 'item':
            if player.get_coins() >= self.items.get(purchase):
                player.add_item(self.items[purchase])
                player.remove_coins(self.items.get(purchase))
            else:
                print(player.get_name(), 'hat nicht genug Geld.'
        if purchase_type=='upgrade':
            if purchase==self.upgrades[0]:
                if player.get_coins() >= Shop.upgrade_cost:
                    player.set_strength(10)
                    player.remove_coins(Shop.upgrade_cost)
                else:
                    print(player.get_name(), 'hat nicht genug Geld.'
                    
            if purchase==self.upgrades[1]:
                if player.get_coins >= Shop.upgrade_cost:
                    player.set_defence(10)
                    player.remove_coins(Shop.upgrade_cost)
                else:
                    print(player.get_name(), 'hat nicht genug Geld.'
            
            if purchase==self.upgrades[2]:
                if player.get_coins >= Shop.upgrade_cost:
                    player.set_aim(10)
                    player.remove_coins(Shop.upgrade_cost)
                else:
                    print(player.get_name(), 'hat nicht genug Geld.'
            
            if purchase==self.upgrades[3]:
                if player.get_coins >= Shop.upgrade_cost:
                    player.set_speed(10)
                    player.remove_coins(Shop.upgrade_cost)
                else:
                    print(player.get_name(), 'hat nicht genug Geld.'
            
                
class Game(object):
    def __init__(self, player1, player2, game_shop):
        self.player1 = player1
        self.player2 = player2
        self.shop = game_shop
        
    def start_round(self):
        if randint(0,1) == 0:
            self.attacking_player = self.player1
            self.defending_player = self.player2
        else:
            self.attacking_player = self.player2
            self.defending_player = self.player1
            
        prompt = (f"{self.attacking_player.get_name()}, Wähle einen Angriff aus:\n"
                 "1: Normaler Angriff (Schaden basiert auf den Attributen)\n"
                 "2: Fish Slap (garantierter Treffer mit wenigen Schaden)\n"
                 "3: Recharge (erhöht den Multiplikator für den nächsten Angriff)\n"
                 "4: Schneeball Rampage (glücksbasierter Schneeballangriff)\n"
                 "5: Stats anzeigen\n"
                 "6: Shop\n"
                 "Zahl zwischen 1 & 6 eingeben: ")
        
        valid_input = False
        while not valid_input:
            attacking_mode = input(prompt)
            
            if attacking_mode == "1":
                damage = self.attacking_player.attack(self.defending_player)
                if damage == -1:
                    print(f"{self.defending_player.get_name()} ist ausgewichen!")
                elif damage == 0:
                    print(f"{self.defending_player.get_name()} hat den Angriff abgewehrt!")
                else:
                    self.defending_player.take_damage(damage)
                    print(f"{self.attacking_player.get_name()} hat {damage} Schaden verursacht!")
                    
                    if not self.defending_player.alive:
                        print(f"{self.defending_player.get_name()} ist tot!")
                valid_input = True

            elif attacking_mode == "2":
                damage = self.attacking_player.fish_slap()
                self.defending_player.take_damage(damage)
                print(f"{self.attacking_player.get_name()} hat {self.defending_player.get_name()} mit einem Fisch abgeworfen! {damage} Schaden verursacht!")
                
                if not self.defending_player.alive:
                    print(f"{self.defending_player.get_name()} ist tot!")
                valid_input = True

            elif attacking_mode == "3":
                multiplier = self.attacking_player.recharge()
                print(f"{self.attacking_player.get_name()} lädt den Multiplikator auf {multiplier}!")
                valid_input = True

            elif attacking_mode == "4":
                damage = self.attacking_player.snowball_rampage()
                if damage == 0:
                    print(f"{self.attacking_player.get_name()} beschwört mehrere Schneebälle, verfehlt aber alle...")
                else:
                    self.defending_player.take_damage(damage)
                    print(f"{self.attacking_player.get_name()} beschwört {damage*100} Schneebälle und wirft alle auf {self.defending_player.get_name()} mit {damage} Schaden!")
                    
                    if not self.defending_player.alive:
                        print(f"{self.defending_player.get_name()} ist tot!")
                valid_input = True
            
            elif attacking_mode == "5":
                print(f"{self.attacking_player.get_name()} Stats:\n"
                    f"Stärke: {self.attacking_player.get_strength()}\n"
                    f"Verteidigung: {self.attacking_player.get_defence()}\n"
                    f"Zielgenauigkeit: {self.attacking_player.get_aim()}\n"
                    f"Geschwindigkeit: {self.attacking_player.get_speed()}\n"
                    f"Lebenspunkte: {self.attacking_player.get_health()}\n")
            else:
                print(f"Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 5.")

if __name__ == "__main__":
    print(f'''__________                            .__         __________.____       _____    ____________________
\______   \ ____   ____    ____  __ __|__| ____   \______   \    |     /  _  \  /   _____/\__    ___/
 |     ___// __ \ /    \  / ___\|  |  \  |/    \   |    |  _/    |    /  /_\  \ \_____  \   |    |   
 |    |   \  ___/|   |  \/ /_/  >  |  /  |   |  \  |    |   \    |___/    |    \/        \  |    |   
 |____|    \___  >___|  /\___  /|____/|__|___|  /  |______  /_______ \____|__  /_______  /  |____|   
               \/     \//_____/               \/          \/        \/       \/        \/            
        _o) (o_
      -./\\\\ //\.-
       _\_U U_/_         ''')
    
    print(f"Hier kämpfen 2 Pinguine gegeneinander! Man kann zwischen mehreren Angriffen auswählen und im Shop die Pinguine upgraden! Jeder Pinguin hat 5 Attribute: Stärke, Verteidigung, Zielgenauigkeit, Geschwindigkeit und Lebenspunkte. Viel Glück!\n")
    
    #ERSTELLUNG DER SPIELER
    player1_type = ""
    while player1_type not in ["1", "2"]:
        player1_type = input(f"Wähle die Art des ersten Pinguins (1: Spieler, 2: Bot): ")
        if player1_type not in ["1", "2"]:
            print(f"Ungültige Eingabe. Bitte wähle 1 oder 2.")
    
    if player1_type == "1":
        player1_name = input(f"Gib den Namen des ersten Pinguins ein: ")
        player1 = Player(player1_name)
    else:  
        player1_name = "Bot_1"
        player1 = Bot(player1_name)

    print(f"Der erste Pinguin ist {player1_name}!")
    print(player1)


    player2_type = ""
    while player2_type not in ["1", "2"]:
        player2_type = input(f"Wähle die Art des zweiten Pinguins (1: Spieler, 2: Bot): ")
        if player2_type not in ["1", "2"]:
            print(f"Ungültige Eingabe. Bitte wähle 1 oder 2.")

    if player2_type == "1":
        player2_name = input(f"Gib den Namen des zweiten Pinguins ein: ")
        while player2_name == player1_name:
            print(f"Der Name ist bereits vergeben. Bitte wähle einen anderen Namen.")
            player2_name = input(f"Gib den Namen des zweiten Pinguins ein: ")
        player2 = Player(player2_name)
    else:
        player2_name = "Bot_2"
        player2 = Bot(player2_name)

    print(f"Der zweite Pinguin ist {player2_name}!")
    print(player2)

    game = Game(player1, player2)
    while player1.alive and player2.alive:
        game.start_round()
    print("Spiel beendet!")