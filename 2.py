class FootBallPlayer:
    def __init__(self, name, posession):
        self.name=name
        self.posession=posession
    def said_hello(self):
        print('Hello, My name is:', self.name, "And I am", self.posession, end='.')
def Man_Unated():
    Player1=FootBallPlayer('Rashford', 'Striker')
    Player2=FootBallPlayer('Martial', 'Striker')
    Player3=FootBallPlayer('James', 'MidFielder')
    Player4=FootBallPlayer('Pogba', 'MidFielder')
    Player5=FootBallPlayer('GreenWood', 'Striker')
    Player6=FootBallPlayer('Fernandesh', 'MidFielder')
    Player7=FootBallPlayer('Lingard', 'MidFielder')
    Player8=FootBallPlayer('Shoy', 'Defender')
    Player9=FootBallPlayer('Maquire', 'Defender')
    Player10=FootBallPlayer('Williams', 'Defender')
    Player11=FootBallPlayer('De Gea', 'GoalKeeper')
    Player1.said_hello()
Man_Unated()