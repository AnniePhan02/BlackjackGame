class Player:
    def __init__(self, name="Player", bankroll=1000):
        self.name = name
        self.hand = []
        self.bankroll = bankroll
        self.bet = 10
