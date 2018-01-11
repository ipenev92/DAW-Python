class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
           return 0
        return 50
    
    @staticmethod
    def ones(*dice):
        sum_ones = 0
        for die in dice:
            if die == 1:
                sum_ones += 1
        return sum_ones
    

    @staticmethod
    def twos(*dice):
        sum_twos = 0
        for die in dice:
            if die == 2:
                sum_twos += 2
        return sum_twos
    
    @staticmethod
    def threes(*dice):
        sum_threes = 0
        for die in dice:
            if die == 3:
                sum_threes += 3
        return sum_threes
    
    @staticmethod
    def fours(*dice):
        sum_fours = 0
        for die in dice:
            if die == 4:
                sum_fours += 4
        return sum_fours

    @staticmethod
    def fives(*dice):
        sum_fives = 0
        for die in dice:
            if die == 5:
                sum_fives += 5
        return sum_fives

    @staticmethod
    def sixes(*dice):
        sum_sixes = 0
        for die in dice:
            if die == 6:
                sum_sixes += 6
        return sum_sixes

    #def fours(self):
    #sum_fours = 0
    #for die in self.dice:
    #if self.dice[die] == 4:
    #sum_fours += 4
    #return sum_fours

    #def fives(self):
    #s = 0
    #i = 0
    #for i in range(len(self.dice)): 
    #if (self.dice[i] == 5):
    #s = s + 5
    #return s
    

    #def sixes(self):
    #sum = 0
    #for at in range(len(self.dice)): 
    #if (self.dice[at] == 6):
    #sum = sum + 6
    #return sum
    
    @staticmethod
    def one_pair(*dice):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0


if __name__ == '__main__':
    #Asserts de la funcion Chance.
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

    #Asserts funcion Yatzy.
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 2, 1)

    #Asserts Ones.
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 1 == Yatzy.ones(3, 5, 1, 3, 2)
    assert 2 == Yatzy.ones(1, 4, 5, 3, 1)
    assert 3 == Yatzy.ones(1, 3, 1, 4, 1)
    assert 4 == Yatzy.ones(1, 1, 2, 1, 1)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

    #Asserts Twos.
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 2 == Yatzy.twos(3, 5, 1, 3, 2)
    assert 4 == Yatzy.twos(2, 4, 2, 3, 1)
    assert 6 == Yatzy.twos(2, 3, 2, 2, 1)
    assert 8 == Yatzy.twos(2, 1, 2, 2, 2)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)

    #Asserts Threes.
    assert 0 == Yatzy.threes(2, 1, 5, 4, 5)
    assert 3 == Yatzy.threes(3, 5, 1, 4, 2)
    assert 6 == Yatzy.threes(1, 3, 5, 3, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 1)
    assert 12 == Yatzy.threes(3, 3, 2, 3, 3)
    assert 15 == Yatzy.threes(3, 3, 3, 3, 3)

    #Assers Fours.
    assert 0 == Yatzy.fours(2, 1, 5, 3, 5)
    assert 4 == Yatzy.fours(3, 2, 1, 4, 2)
    assert 8 == Yatzy.fours(6, 4, 5, 4, 1)
    assert 12 == Yatzy.fours(3, 4, 3, 4, 4)
    assert 16 == Yatzy.fours(3, 4, 4, 4, 4)
    assert 20 == Yatzy.fours(4, 4, 4, 4, 4)

    #Asserts Fives.
    assert 0 == Yatzy.fives(2, 1, 6, 4, 3)
    assert 5 == Yatzy.fives(3, 5, 1, 4, 2)
    assert 10 == Yatzy.fives(1, 3, 5, 5, 1)
    assert 15 == Yatzy.fives(3, 5, 5, 5, 1)
    assert 20 == Yatzy.fives(5, 5, 5, 5, 3)
    assert 25 == Yatzy.fives(5, 5, 5, 5, 5)

    #Asserts Sixes.
    assert 0 == Yatzy.sixes(2, 1, 5, 4, 5)
    assert 6 == Yatzy.sixes(6, 5, 1, 4, 2)
    assert 12 == Yatzy.sixes(6, 6, 5, 3, 1)
    assert 18 == Yatzy.sixes(6, 3, 6, 6, 1)
    assert 24 == Yatzy.sixes(3, 6, 6, 6, 6)
    assert 30 == Yatzy.sixes(6, 6, 6, 6, 6)