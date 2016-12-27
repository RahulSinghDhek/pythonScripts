#!/usr/bin/python
from collections import defaultdict

class Player:
    totalSpent = defaultdict(int)
    totalGames	= defaultdict(int) 
    def __init__(self,name,phoneNo,amount):
	self.name=name
	self.phoneNo=phoneNo
	self.amount = amount
	Player.totalSpent[name]=Player.totalSpent[name]+amount
	Player.totalGames[name]=Player.totalGames[name]+1

    def displayCount(self):
        print "Total Players %d" % Player.playerCount

class Game:

    
    def __init__(self,gameId,playerList,totalAmount):
	self.gameId=gameId
	self.playerList= playerList
	self.totalAmount = totalAmount
    def perHeadGameWise(self):
	noOfPlayerForGame =  len(self.playerList)
	return (self.totalAmount/noOfPlayerForGame)
	
    def partOfGame(self,playerName):
	for player in self.playerList:
	    if playerName in player:
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

print game1.partOfGame("vikalp")
print game1.partOfGame("Uma")
print game1.partOfGame("rejy")
print game1.partOfGame("Rivu")

print "Vikalp : " , Player.totalSpent['vikalp']/Player.totalGames['vikalp']
print "Rivu   : " , Player.totalSpent['Rivu']/Player.totalGames['Rivu']

