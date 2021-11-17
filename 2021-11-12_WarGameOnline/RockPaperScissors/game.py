class Game:

    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]

    def get_Player_move(self, p):
        """

        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def player(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True
    
    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        pass
        #return winner
    
    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
