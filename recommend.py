class contentscore:

    def __init__(self, motivate,newthing,cheering ,food,social,resting,meditaion,suicide):
        self.motivate = motivate
        self.newthing = newthing
        self.cheering = cheering
        self.food = food
        self.social = social
        self.resting = resting
        self.meditaion = meditaion
        self.suicide = suicide

     # class method for object
    def getVolume(self):
        return self.width * self.height * self.dept

    @staticmethod
    def compare(a, b):
        if a.getVolume() > b.getVolume():
            return 'greater than'
        elif a.getVolume() == b.getVolume():
            return 'equal'
        else:
            return 'less than'

            

# a = contentscore(2, 3, 4)
# b = contentscore(1, 2, 5)

# contentscore.color = 'red'

# print('Box a volume = %d' % a.getVolume())
# print('Box b volume = %d' % b.getVolume())

# print('Box a color = %s' % a.color)
# print('Box b color = %s' % b.color)

# print('Box a volume a is %s box b' % Box.compare(a, b))