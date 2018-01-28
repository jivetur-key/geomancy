from random import randint

class Generate(object):

    """generates the figures of the reading"""

    def __init__(self):
        self.geo = [[]]

    def set_matrix(self):

        """creates a matrix of four columns and six-teen rows each row equals one figure"""
        self.geo = [[0]*4 for i in range(15)]

    def set_mothers(self):
        """The first four figures or the first four roles each figure is made up four elements that are randomly generated even or od numbers"""
        for i in range(4):
            for j in range(4):
                self.geo[i][j] = randint(1,2)

    def set_daughters(self):
        """the daughters are the next four figures or rows three - seven they are transpose of the first four figures"""
        x = 4
        for i in range(4):
            for j in range(4):
                self.geo[x][j] = self.geo[j][i]
            x += 1

    def set_resultants(self):

        """->the resultants are the next four figures or eight - eleven, in this case it will include the remaining figures; the left and right witnesses, and the judge.  That is that they use the same even or formula.  The rows are compared in pairs whether the elements are equal or not. If equal the new element is even, if not odd<-"""

        x = 8
        for i in range(0,13,2):
            for j in range(4):
                if self.geo[i][j] != self.geo[i+1][j]:
                    self.geo[x][j] = 1
                else:
                    self.geo[x][j] = 2
            x += 1

    def _generate(self):

        """executes the objects code"""

        self.set_matrix()
        self.set_mothers()
        self.set_daughters()
        self.set_resultants()
