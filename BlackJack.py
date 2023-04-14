class BlackJack():
    
    #Variables asked when create BlackJack instance
    def __init__(self,player):
            self.player = player
            self.balance = 0
            
    def StartGame(self):
        self.AddMoney()
        print("Ok, we can start playing {}".format(self.player))
        self.PutBet()
        player_result = self.ShuffleCards(self.player)
        dealer_result = self.ShuffleCards('Dealer')
        if self.AddCards() == 1:
            player_result += self.SuffleCards(1)




        
    def AddCards(self):
        while True:
            try:
                self.addcard = int(input('Do you want another card? 1 for yes 0 for no'))
            except:
                print('Try with a number')
                continue
            else:
                break

    def AddMoney(self):
        while True:
            try:
                self.amnt_deposit = int(input("How much do you want to add to you account: "))
                ###############################
                ### ADD CODE TO CHECK FOR NEGATIVE NUMBERS ###
                ###############################
                self.balance += self.amnt_deposit
            except:
                print("Try with a number\n")
                continue
            else:
                print("You now have {} dollars to play\n".format(self.balance))
                break
                
    def PutBet(self):
        self.bet = 0
        while True:
            try:
                amnt_bet = int(input("How much do you want to bet: "))
                self.bet += amnt_bet
            except:
                print("Try with a number\n")
                continue
            else:
                print("Bet placed: {}\n".format(self.bet))
                break
        
        
    def ShuffleCards(self,player,cards=0):
        self.player = player
        self.cards = cards
        result = True 
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
                'Ten', 'Jack', 'Queen', 'King', 'Ace']
        values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        
        import random
        random_suit = suits[random.randint(0,len(suits)-1)]
        random_rank = ranks[random.randint(0,len(ranks)-1)]
        random_suit2 = suits[random.randint(0,len(suits)-1)]
        random_rank2 = ranks[random.randint(0,len(ranks)-1)]
        if self.player == 'Dealer' or self.cards == 1:
            print("{} cards are: {} of {}".format(self.player, random_rank,random_suit))
            self.sum_cards = self.CheckResult(values[random_rank])
            return self.sum_cards
        else:
            print("{} cards are: {} of {} and {} of {}".format(self.player, random_rank,random_suit, 
            random_rank2,random_suit))
            self.sum_cards = self.CheckResult(values[random_rank], values[random_rank2])
            return self.sum_cards


    def CheckResult(self,card1,card2=0):
        self.card1 = card1
        self.card2 = card2
        total = sum(self.card1, self.card2)
        return total


play_bj = BlackJack(player = "Carlos")
play = play_bj.StartGame()
