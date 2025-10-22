import random
class Coin():

    def __init__(self):
        self.amount=20
        self.sideup=random.choice(["Heads","Tails"])
    
    def toss(self):
        value=random.randint(0,1)
        if value==0:
            self.sideup="Heads"
        else:
            self.sideup="Tails"
        return self.sideup
    
    def get_sideup(self):
        return self.sideup
    
    def get_amount(self):
        return self.amount
    
    def set_amount(self,change):
        if change in [1,-1]:
            self.amount+=change 
            
        
def main():
    player_1=Coin()
    player_2=Coin()
    validation=input("Do you want to play(answer Y or y for yes)")
    while validation.lower()=="y":
        p1_toss=player_1.toss()
        p2_toss=player_2.toss()
        print(f'Player 1 tossed:{p1_toss}')
        print(f'Player 2 tossed:{p2_toss}')
       
        if p1_toss==p2_toss:
            player_1.set_amount(+1)
            player_2.set_amount(-1)
            print("Coins matched! Player1 gets Player2’s coin.")
        else:
            player_2.set_amount(+1)
            player_1.set_amount(-1)
            print("Coins didn't match! Player 2 gets Player 1’s coin.")
        print(f"Player 1 has {player_1.get_amount()} coins remaining")
        print(f"Player 2 has {player_2.get_amount()} coins remaining")
       
        validation=input("Do you want to continue?")
    
    player1_final_amount=player_1.get_amount() 
    player2_final_amount=player_2.get_amount()    
    if player1_final_amount > player2_final_amount:
     print("Player 1 won!")
    else:
        print("Player 2 won!")


if __name__=="__main__":
    main()




