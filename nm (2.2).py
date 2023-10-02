#define the base class player
class player:
  def play(self):
    print("the player is playing cricket.")
#define the derived class Batsman  
class Batsman(player):
  def Play(self):
    print("the bat man is batting.")
#define the derived class Bowler
class Bowler(player):
  def play(self):
    print("the bowler is bowling. ")
#create objects of Batsman and object
batsman=Batsman()
bowler=Bowler()
#call the play()method for each object
batsman.play()
bowler. play()
      
