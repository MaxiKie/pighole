
import random

class player:
    def __init__(self, name, strat):
        self.name = name
        self.strat = strat
        self.num = 10
        self.wins = 0

class game:
    def __init__(self):
        self.slot_1=self.slot_2=self.slot_3=self.slot_4=self.slot_5=0
        self.n_rounds=1000
        self.game_over=False
        self.full_pits=0 #Anzahl vollepits
        self.n_pigs=0 #Anzahl Pigs auf Spielbrett

    def wurf(self,player):
        again = True
        augenzahl = random.randint(1,6)
        #with open('game_summary.txt', 'a') as f:
        #    f.write('Würfel: '+str(augenzahl)+'\n')
        if augenzahl == 6:
            player.num-=1
        elif augenzahl == 5 and self.slot_5<5:
                player.num-=1
                self.slot_5+=1
        elif augenzahl == 4 and self.slot_4<4:
                player.num-=1
                self.slot_4+=1
        elif augenzahl == 3 and self.slot_3<3:
                player.num-=1
                self.slot_3+=1
        elif augenzahl == 2 and self.slot_2<2:
                player.num-=1
                self.slot_2+=1
        elif augenzahl == 1 and self.slot_1<1:
                player.num-=1
                self.slot_1+=1
        else:
            #Verzockt
            player.num=player.num+self.slot_1+self.slot_2+self.slot_3+self.slot_4+self.slot_5
            self.slot_1=self.slot_2=self.slot_3=self.slot_4=self.slot_5=0
            self.full_pits=0
            again=False
        return player,again

    def refresh_game_stats(self):
        if self.slot_1==1:
            self.full_pits+=1
        if self.slot_2==2:
            self.full_pits+=1
        if self.slot_3==3:
            self.full_pits+=1
        if self.slot_4==4:
            self.full_pits+=1
        if self.slot_5==5:
            self.full_pits+=1
        self.n_pigs=self.slot_1+self.slot_2+self.slot_3+self.slot_4+self.slot_5
    
    def plot(self):
        #1
        if self.slot_1==1:
             plot_slot_1='{X}'
        elif self.slot_1==0:
             plot_slot_1='{O}'
        #2
        if self.slot_2==2:
             plot_slot_2='{XX}'
        elif self.slot_2==1:
             plot_slot_2='{XO}'
        elif self.slot_2==0:
             plot_slot_2='{OO}'
        #3
        if self.slot_3==3:
             plot_slot_3='{XXX}  '
        elif self.slot_3==2:
             plot_slot_3='{XXO}  '
        elif self.slot_3==1:
             plot_slot_3='{XOO}  '
        elif self.slot_3==0:
             plot_slot_3='{OOO}  '
        #4
        if self.slot_4==4:
             plot_slot_4='{XXXX}'
        elif self.slot_4==3:
             plot_slot_4='{XXXO}'
        elif self.slot_4==2:
             plot_slot_4='{XXOO}'
        elif self.slot_4==1:
             plot_slot_4='{XOOO}'
        elif self.slot_4==0:
             plot_slot_4='{OOOO}'
        #5
        if self.slot_5==5:
             plot_slot_5='{XXXXX}'
        elif self.slot_5==4:
             plot_slot_5='{XXXXO}'
        elif self.slot_5==3:
             plot_slot_5='{XXXOO}'
        elif self.slot_5==2:
             plot_slot_5='{XXOOO}'
        elif self.slot_5==1:
             plot_slot_5='{XOOOO}'
        elif self.slot_5==0:
             plot_slot_5='{OOOOO}'

        plot=plot_slot_1+'\n'+plot_slot_2+'\n'+plot_slot_3+'\n'+plot_slot_4+'\n'+plot_slot_5+'\n'
        return plot



def zug(game,player):
    again = True
    first_move=True
    while (again and game.full_pits/6 < player.strat) or first_move:#Definiere Ausstiegsbedingung player 1
        player,again=game.wurf(player)
        first_move=False
        if player.num==0:
            #with open('game_summary.txt', 'a') as f:
            #    f.write(player.name+' gewinnt!\n')
            player.wins+=1
            game.game_over=True
            again=False
        game.refresh_game_stats()
        return player

max_games=1000
max_strats=10000

for i in range(max_strats):
    p1=player(name='P1',strat=random.uniform(0,1))
    p2=player(name='P2',strat=random.uniform(0,1))
    p3=player(name='P3',strat=random.uniform(0,1))
    p4=player(name='P4',strat=random.uniform(0,1))
    #Reset gene_summary.txt
    with open('game_summary.txt', 'w') as f:
                f.write('')

    
    for n_game in range(max_games):
        #with open('game_summary.txt', 'a') as f:
        #    f.write('------ GAME '+str(n_game)+' ------\n')
        p1.num=p2.num=p3.num=p4.num=10

        game1=game()
        i=0
        player_array = [p1,p2,p3,p4]
        index = random.randint(0,3)

        while not game1.game_over and i<game1.n_rounds:
            index +=1
            if index == 4:
                 index = 0

            #with open('game_summary.txt', 'a') as f:
            #    f.write('--- Am Zug: '+player_array[index].name+' ---\n')
            #    f.write('Spielfeld:\n')
            #    f.write(game1.plot()+'\n')
            player_array[index] = zug(game1,player_array[index])
            if game1.game_over:#wenn spieler 1 gewonnen hat, darf spieler 2 nicht nochmal
                break
            

    #with open('output_summary.txt', 'w') as f:
    #    f.write('player 1: Wins: '+str(p1.wins)+', Strat: '+str(p1.strat)+'\n')
    #    f.write('player 2: Wins: '+str(p2.wins)+', Strat: '+str(p2.strat)+'\n')
    #    f.write('player 3: Wins: '+str(p3.wins)+', Strat: '+str(p3.strat)+'\n')
    #    f.write('player 4: Wins: '+str(p4.wins)+', Strat: '+str(p4.strat)+'\n')
    #    f.write('--------------------------')

    with open('stats.csv', 'a') as f:
        f.write(str(p1.wins/max_games)+';'+str(p1.strat)+'\n')
        f.write(str(p2.wins/max_games)+';'+str(p2.strat)+'\n')
        f.write(str(p3.wins/max_games)+';'+str(p3.strat)+'\n')
        f.write(str(p4.wins/max_games)+';'+str(p4.strat)+'\n')

    