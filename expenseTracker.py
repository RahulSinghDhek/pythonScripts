#!/usr/bin/python
from collections import defaultdict

class Player:
    totalDeposited = defaultdict(int)
    totalGames	= defaultdict(int) 
    def __init__(self,name,phoneNo,amount):
	self.name=name
	self.phoneNo=phoneNo
	self.amount = amount
	Player.totalDeposited[name]=Player.totalDeposited[name]+amount
	Player.totalGames[name]=Player.totalGames[name]+1

class Game:

    totalAmountPerGame = 0
    def __init__(self,gameId,playerList,totalAmount):
	self.gameId=gameId
	self.playerList= playerList
	self.totalAmount = totalAmount
	Game.totalAmountPerGame = Game.totalAmountPerGame + totalAmount
    def perHeadGameWise(self):
	noOfPlayerForGame =  len(self.playerList)
	return (self.totalAmount/noOfPlayerForGame)
	
    def isPartOfGame(self,playerName):
	for playerDetail in self.playerList:
	    if(playerDetail.name == playerName):
		return True
	return False


listOfPlayers={}
listOfPlayers['3Dec2016']= [Player("rahul",12345,1000.0),Player("Uma",12346,300.0),Player("vikalp",12347,400.0),Player("Rivu",12348,200.0)]
listOfPlayers['10Dec2016']= [Player("rahul",12345,0.0),Player("Uma",12346,300.0),Player("vikalp",12347,0.0),Player("Rivu",12348,200.0)]
listOfPlayers['17Dec2016']= [Player("rahul",12345,0.0),Player("Uma",12346,0.0),Player("Rk",12377,400.0),Player("lynal",12358,200.0)]
listOfPlayers['24Dec2016']= [Player("rahul",12345,0.0),Player("Deep",12396,0.0),Player("vikalp",12347,0.0),Player("Rejy",12378,0.0)]
listOfPlayers['31Dec2016']= [Player("rahul",12345,0.0),Player("Uma",12346,0.0),Player("sudeep",12357,400.0),Player("Rejy",12378,800.0)]

game1 = Game("3Dec2016",listOfPlayers['3Dec2016'],1000.0)
game2 = Game("10Dec2016",listOfPlayers['10Dec2016'],1500.0)
game3 = Game("17Dec2016",listOfPlayers['17Dec2016'],1000.0)
game4 = Game("24Dec2016",listOfPlayers['24Dec2016'],1500.0)
game5 = Game("31Dec2016",listOfPlayers['31Dec2016'],1000.0)

print game1.perHeadGameWise()
print game2.perHeadGameWise()
print game3.perHeadGameWise()
print game4.perHeadGameWise()
print game5.perHeadGameWise()

print game1.isPartOfGame("vikalp")
print game1.isPartOfGame("Uma")
print game1.isPartOfGame("rejy")
print game1.isPartOfGame("Rivu")

gameList=[game1,game2,game3,game4,game5]
#print "Vikalp : " , Player.totalSpent['vikalp']/Player.totalGames['vikalp']
#print "Rivu   : " , Player.totalSpent['Rivu']/Player.totalGames['Rivu']
totalExp = defaultdict(int)
for x in gameList:
    if (x.isPartOfGame("vikalp")):
	totalExp['vikalp'] = totalExp['vikalp'] + x.perHeadGameWise()
    if (x.isPartOfGame("Rivu")):
	totalExp['Rivu'] = totalExp['Rivu'] + x.perHeadGameWise()
    if (x.isPartOfGame("rahul")):
	totalExp['rahul'] = totalExp['rahul'] + x.perHeadGameWise()
    if (x.isPartOfGame("Uma")):
	totalExp['Uma'] = totalExp['Uma'] + x.perHeadGameWise()
    if (x.isPartOfGame("Deep")):
	totalExp['Deep'] = totalExp['Deep'] + x.perHeadGameWise()
    if (x.isPartOfGame("sudeep")):
	totalExp['sudeep'] = totalExp['sudeep'] + x.perHeadGameWise()
    if (x.isPartOfGame("Rejy")):
	totalExp['Rejy'] = totalExp['Rejy'] + x.perHeadGameWise()
    if (x.isPartOfGame("lynal")):
	totalExp['lynal'] = totalExp['lynal'] + x.perHeadGameWise()
    if (x.isPartOfGame("Rk")):
	totalExp['Rk'] = totalExp['Rk'] + x.perHeadGameWise()


print "vikalp balance : " , Player.totalDeposited['vikalp']-totalExp['vikalp']
print "rahul balance : " , Player.totalDeposited['rahul']-totalExp['rahul']
print "Rivu balance : " , Player.totalDeposited['Rivu']-totalExp['Rivu']
print "Uma balance : " , Player.totalDeposited['Uma']-totalExp['Uma']
print "Deep balance : " , Player.totalDeposited['Deep']-totalExp['Deep']
print "sudeep balance : " , Player.totalDeposited['sudeep']-totalExp['sudeep']
print "lynal balance : " , Player.totalDeposited['lynal']-totalExp['lynal']
print "Rejy balance : " , Player.totalDeposited['Rejy']-totalExp['Rejy']
print "Rk balance : " , Player.totalDeposited['Rk']-totalExp['Rk']


print "Net Amount on per game basis : " , Game.totalAmountPerGame
print "Net Balance on game basis :    " , sum(Player.totalDeposited.values())- Game.totalAmountPerGame


    
