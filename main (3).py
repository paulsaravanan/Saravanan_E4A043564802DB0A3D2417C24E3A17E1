classPlayer:

defplay(self):

print("Theplayerisplayingcricket.")

classBatsman(Player):

defplay(self):

print("Thebatsmanisbatting.")

classBowler(Player):

defplay(self):

print("Thebowlerisbowling.")

batsman=Batsman()

bowler=Bowler()

batsman.play()

bowler.play()