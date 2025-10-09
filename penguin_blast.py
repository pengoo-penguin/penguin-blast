# -*- coding: utf-8 -*-
from random import randint

class Penguin(object):
    MAX_HEALTH = 100
    __slots__ = ['_Penguin__strength', '_Penguin__defence', '_Penguin__aim', '_Penguin__speed', '_Penguin__healthpoints', '_Penguin__multiplier', '_Penguin__coins', '_Penguin__inventory', 'status', 'max_health','wins', 'alive']
    
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

        self.wins = 0
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
        elif self.status == 'happy':
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
            damage = snowballs * 0.01 * self.__strength
            return damage


        
class Player(Penguin):
    __slots__ = ['_Player__name']
    def __init__(self, name):
        Penguin.__init__(self)
        self.__name = name
    
    def get_name(self):
        return self.__name
        

class Bot(Penguin):
    __slots__ = ['_Bot__name']
    def __init__(self, name):
        Penguin.__init__(self)
        self.__name = name

    def get_name(self):
        return self.__name

    def choose_action(self, opponent):
        if self.get_coins() >= 10:
            return "6"  
        
        health_ratio = self.get_health() / Penguin.MAX_HEALTH
        if health_ratio < 0.3 and "Medizinkoffer" in self.get_inventory():
            return "6"  
        elif health_ratio < 0.5:
            if self.multiplier > 4:
            		return "1"
            else	:
                return "3"  
        elif opponent.get_health() < 20:
            return "1"  
        else:
            return "4"
            
    def choose_purchase(self):
        coins = self.get_coins()
        health = self.get_health()
        
        if health < 30 and coins >= 60:
            return 7  
        elif coins >= 70:
            return 8  
        elif coins >= 40:
            return 5 
        elif coins >= 20:
            return 3  
        elif coins >= 10:
            return 2
        
        return None


class Shop(object):
    upgrade_cost = 10 
    def __init__(self):
        self.items = {
             1: 10,  # Unsichtbarkeitsumhang
             2: 10,  # Pflaster
             3: 20,  # Pfeil & Bogen
             4: 30,  # Kettensäge
             5: 40,  # Pistole
             6: 50,  # Auto
             7: 60,  # Medizinkoffer
             8: 70,  # Superman Anzug
        }
        self.upgrades = [
            'Stärke',
            'Verteidigung',
            'Zielgenauigkeit', 
            'Geschwindigkeit'
        ]

    def buy(self, player, purchase_type, purchase):
        if purchase_type == 'item':
            if purchase in self.items:
                cost = self.items[purchase]
                if player.get_coins() >= cost:
                    player.remove_coins(cost)
                    player.add_item(purchase)
                    print(f"{player.get_name()} hat Item {purchase} gekauft!")
                    return True
                else:
                    print(f"{player.get_name()} hat nicht genug Geld.")
                    return False
            
        elif purchase_type == 'upgrade':
            if purchase in self.upgrades:
                if player.get_coins() >= self.upgrade_cost:
                    if purchase == 'Stärke':
                        player.set_strength(10)
                    elif purchase == 'Verteidigung':
                        player.set_defence(10)
                    elif purchase == 'Zielgenauigkeit':
                        player.set_aim(10)
                    elif purchase == 'Geschwindigkeit':
                        player.set_speed(10)
                    player.remove_coins(self.upgrade_cost)
                    print(f"{player.get_name()} hat {purchase} verbessert!")
                    return True
                else:
                    print(f"{player.get_name()} hat nicht genug Geld.")
                    return False
            else:
                print(f"{purchase} ist kein gültiges Upgrade.")
                return False
    
    def __str__(self):
        return f'''
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        –––––––––––––––––––––––– SHOP ––––––––––––––––––––––––––––
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (1) Unsichtbarkeitsumhang                           10 💵
        (Der Pinguin wird unsichtbar und 
        kann nicht getroffen werden)
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (2) Pflaster                                        10 💵
        (Heilt 10 HP (nur einmalig nutzbar))
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (3) Pfeil & Bogen                                   20 💵
        (Erhalte Pfeil und Bogen für den
        Rest der Runde und erziele doppelt
        so vielen Schaden!)
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (4) Kettensäge                                      30 💵
        (Erhalte eine Kettensäge für den 
        Rest der Runde und erziele 3x so
        vielen Schaden!)
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (5) Pistole                                         40 💵
        (Erhalte eine Pistole für den
        Rest der Runde der 4x so viel
        Schaden macht! )
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (6) Auto                                            50 💵
        (Fahre für den Rest der Runde mit 
        einem Auto rum und erschwere 
        deinen Gegner so, dich zu
        treffen!)
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (7) Medizinkoffer                                   60 💵
        (Heilt den Pinguin komplett!)
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (8) Superman Anzug                                  70 💵
        (Werde stärker & schneller & 
        robuster für den ganzen Rest 
        der Runde)
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (9) Stärke Upgrade                                   10 💵
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (10) Verteidigung Upgrade                            10 💵
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (11) Zielgenauigkeit Upgrade                         10 💵
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        (12) Geschwindigkeit Upgrade                         10 💵
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        '''
            
                
class Game(object):
    def __init__(self, player1, player2, game_shop):
        self.player1 = player1
        self.player2 = player2
        self.shop = game_shop
        
        if randint(0,1) == 0:
            self.attacking_player = self.player1
            self.defending_player = self.player2
            print(f"\n{self.player1.get_name()} greift zuerst an!")
        else:
            self.attacking_player = self.player2
            self.defending_player = self.player1
            print(f"\n{self.player2.get_name()} greift zuerst an!")

    def start_turn(self):

        prompt = (f"\n{self.attacking_player.get_name()}, Wähle einen Angriff aus:\n"
                 "1: Normaler Angriff (Schaden basiert auf den Attributen)\n"
                 "2: Fish Slap (garantierter Treffer mit wenigen Schaden)\n"
                 "3: Recharge (erhöht den Multiplikator für den nächsten Angriff)\n"
                 "4: Schneeball Rampage (glücksbasierter Schneeballangriff)\n"
                 "5: Stats anzeigen\n"
                 "6: Shop\n"
                 "Zahl zwischen 1 & 6 eingeben: ")
        
        valid_input = False
        while not valid_input:
            if isinstance(self.attacking_player, Bot):
                attacking_mode = self.attacking_player.choose_action(self.defending_player)
                print(f"\n{self.attacking_player.get_name()} wählt Aktion {attacking_mode}")
            else:
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
                
                print(self.attacking_player.get_name())
                self.attacking_playeer.status = 'happy'
                print(self.attacking_player)
                
                print(\nself.defending_player.get_name())
                self.defending_player.status = 'slapped'
                print(self.defending_player)
                
                if not self.defending_player.alive:
                    print(f"{self.defending_player.get_name()} ist tot!")
                    print(self.defending_player)
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
                    print(f"{self.attacking_player.get_name()} beschwört mehrere ‚Schneebälle und trifft mit {damage} Schaden!")
     
                    if not self.defending_player.alive:
                        print(f"{self.defending_player.get_name()} ist tot!")
                valid_input = True
            
            elif attacking_mode == "5":
                print(f"\n{self.attacking_player.get_name()} Stats:\n"
                    f"Stärke: {self.attacking_player.get_strength()}\n"
                    f"Verteidigung: {self.attacking_player.get_defence()}\n"
                    f"Zielgenauigkeit: {self.attacking_player.get_aim()}\n"
                    f"Geschwindigkeit: {self.attacking_player.get_speed()}\n"
                    f"Lebenspunkte: {self.attacking_player.get_health()}/{Penguin.MAX_HEALTH}\n"
                    f"Geld: {self.attacking_player.get_coins()} 💵\n")

            elif attacking_mode == "6":
                print(self.shop) 
                if isinstance(self.attacking_player, Bot):
                    purchase = self.attacking_player.choose_purchase()
                    if purchase:
                        self.shop.buy(self.attacking_player, 'item', purchase)
                    else:
                        print(f"{self.attacking_player.get_name()} hat nicht genug Geld für Einkäufe.")
                    valid_input = True
                else:
                    print(f"{self.attacking_player.get_name()}, du hast {self.attacking_player.get_coins()} 💵.")
                    purchase = ''
                    while not purchase.isdigit() or int(purchase) not in range(1, 13):
                        purchase = input('Gebe eine Zahl zwischen 1 und 12 ein (oder 0 wenn du nichts kaufen willst): ')
                        if purchase == '0':
                            print(self.attacking_player.get_name() + " hat nichts gekauft.")
                            break
                        if not purchase.isdigit() or int(purchase) not in range(1, 13):
                            print('Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 12 (oder halt 0)')
                    if purchase != '0':
                        purchase_num = int(purchase)
                        if purchase_num <= 8:
                            self.shop.buy(self.attacking_player, 'item', purchase_num)
                        else:
                            upgrades = {
                                9: 'Stärke',
                                10: 'Verteidigung', 
                                11: 'Zielgenauigkeit',
                                12: 'Geschwindigkeit'
                            }
                            self.shop.buy(self.attacking_player, 'upgrade', upgrades[purchase_num])
                        valid_input = True
            else:
                print(f"Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 6.")
                attacking_mode = ''

        if self.attacking_player.alive and self.defending_player.alive:
            self.attacking_player, self.defending_player = self.defending_player, self.attacking_player

if __name__ == "__main__":
    # Zeige Titel nur einmal
    print(f'''__________                            .__         __________.____       _____    ____________________
\______   \ ____   ____    ____  __ __|__| ____   \______   \    |     /  _  \  /   _____/\__    ___/
 |     ___// __ \ /    \  / ___\|  |  \  |/    \   |    |  _/    |    /  /_\  \ \_____  \   |    |   
 |    |   \  ___/|   |  \/ /_/  >  |  /  |   |  \  |    |   \    |___/    |    \/        \  |    |   
 |____|    \___  >___|  /\___  /|____/|__|___|  /  |______  /_______ \____|__  /_______  /  |____|   
               \/     \//_____/               \/          \/        \/       \/        \/            
        _o) (o_
      -./\\\\ //\.-
       _\_U U_/_         ''')
    
    print(f"Kämpft als Pinguine gegeneinader! Man kann zwischen mehreren Angriffen auswählen und im Shop die Pinguine upgraden!")
    print(f"Jeder Pinguin hat 5 Attribute: Stärke, Verteidigung, Zielgenauigkeit, Geschwindigkeit und Lebenspunkte.")
    print(f"Der erste Pinguin, der 2 Runden gewinnt, gewinnt das Spiel! Viel Glück!\n")
    
    
    keep_playing = True
    
    while keep_playing:
        
        player1_type = ""
        while player1_type not in ["1", "2"]:
            player1_type = input(f"\nWähle die Art des ersten Pinguins (1: Spieler, 2: Bot): ")
            if player1_type not in ["1", "2"]:
                print(f"Ungültige Eingabe. Bitte wähle 1 oder 2.")
        
        if player1_type == "1":
            player1_name = input(f"Gib den Namen des ersten Pinguins ein: ")
            player1 = Player(player1_name)
        else:  
            player1_name = "Bot_1"
            player1 = Bot(player1_name)

        print(f"\nDer erste Pinguin ist {player1_name}!")
        print(player1)

        player2_type = ""
        while player2_type not in ["1", "2"]:
            player2_type = input(f"\nWähle die Art des zweiten Pinguins (1: Spieler, 2: Bot): ")
            if player2_type not in ["1", "2"]:
                print(f"Ungültige Eingabe. Bitte wähle 1 oder 2.")

        if player2_type == "1":
            player2_name = input(f"Gib den Namen des zweiten Pinguins ein: ")
            while player2_name == player1_name:
                print(f"Der Name ist bereits vergeben. Bitte wähle einen anderen Namen.")
                player2_name = input(f"Gib den Namen des zweiten Pinguins ein: ")
            player2 = Player(player2_name)
        else:
            if player1_name == "Bot_1":
                player2_name = "Bot_2"
            else:
                player2_name = "Bot_1"
            player2 = Bot(player2_name)

        print(f"\nDer zweite Pinguin ist {player2_name}!")
        print(player2)

        shop = Shop()
        

        rounds_to_win = 2
        round_number = 1
        
        while player1.wins < rounds_to_win and player2.wins < rounds_to_win:

            print(f"{player1.get_name()}: {player1.wins} Siege | {player2.get_name()}: {player2.wins} Siege".center(60))

            

            player1._Penguin__healthpoints = Penguin.MAX_HEALTH
            player1.alive = True
            player1.status = 'normal'
            
            player2._Penguin__healthpoints = Penguin.MAX_HEALTH
            player2.alive = True
            player2.status = 'normal'
            

            game = Game(player1, player2, shop)
            turn_counter = 0
            

            while player1.alive and player2.alive:
                game.start_turn()
                turn_counter += 1
            

            if player1.alive:
                player1.wins += 1
                winner = player1
                loser = player2
                print(f"\n {player1.get_name()} gewinnt Runde #{round_number}! ")
            else:
                player2.wins += 1
                winner = player2
                loser = player1
                print(f"\n {player2.get_name()} gewinnt Runde #{round_number}! ")
            

            winner_coins = 50 + (turn_counter * 5)
            loser_coins = 20
            
            winner.add_coins(winner_coins)
            loser.add_coins(loser_coins)
            
            print(f" {winner.get_name()} erhält {winner_coins} 💵")
            print(f" {loser.get_name()} erhält {loser_coins} 💵")
            

            if player1.wins >= rounds_to_win or player2.wins >= rounds_to_win:
                break

            
            round_number += 1
            
            if player1.wins < rounds_to_win and player2.wins < rounds_to_win:
                input("\n Drücke Enter für die nächste Runde")
        

    
        
        if player1.wins >= rounds_to_win:
			print('Das Spiel ist vorbei')
            print(player1.get_name(), 'hat das Spiel gewonenn)
            player1.status = 'happy'
            print(player1)
        else:
			print('Das Spiel ist vorbei')
            print(player2.get_name(), 'hat das Spiel gewonenn)
			player2.status = 'happy'
            print(player2)
        
        print(f"\nEndstand: {player1.get_name()} {player1.wins} : {player2.wins} {player2.get_name()}")
        


        play_again = ""
        while play_again not in ["j", "n"]:
            play_again = input("Nochmal spielen? (j/n): ").lower()
            if play_again not in ["j", "n"]:
                print("Bitte 'j' für Ja oder 'n' für Nein eingeben.")
        
        if play_again == "n":
            keep_playing = False
            print("\n🐧 Danke fürs Spielen! Bis zum nächsten Mal! 🐧")
        else:
            print("\n" + "="*60)
            print("🔄 NEUES SPIEL STARTET! 🔄".center(60))
            print("="*60)
