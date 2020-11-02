from interval import Interval


class att_trial():

    def __init__(self, name, **kwargs):
        self.name = name
        self.level = sum(kwargs['level'])
        self.size = len(kwargs['level'])
        try:
            self.average = (sum(kwargs['percentage']) / len(kwargs['percentage'])) * 100
        except:
            self.average = 0

    def decide(self):
        if self.average != 0:
            if (self.level <= 3 and self.size != 1) or (self.level == 1 and self.size == 1):
                return self.low()
            if (self.level == 4 and self.size != 1) or (self.level == 2 and self.size == 1):
                return self.middle()
            if (self.level >= 5 and self.size != 1) or (self.level == 3 and self.size == 1):
                return self.high()

    def low(self):

        if self.average in Interval(97.15, 100.00):
            return 3
        if self.average in Interval(88.58, 97.15):
            return 4
        if self.average in Interval(71.44, 88.58):
            return 5
        if self.average in Interval(42.87, 71.44):
            return 6
        if self.average in Interval(0, 42.87):
            return 7

    def middle(self):

        if self.average in Interval(85.65, 100.00):
            return 8
        if self.average in Interval(68.53, 88.65):
            return 9
        if self.average in Interval(50.04, 68.53):
            return 10
        if self.average in Interval(31.55, 50.04):
            return 11
        if self.average in Interval(14.43, 31.55):
            return 12
        if self.average in Interval(0, 14.43):
            return 13
        pass

    def high(self):
        if self.average in Interval(97.15, 100.00):
            return 18
        if self.average in Interval(88.58, 97.15):
            return 17
        if self.average in Interval(71.44, 88.58):
            return 16
        if self.average in Interval(42.87, 71.44):
            return 15
        if self.average in Interval(0, 42.87):
            return 14



