
class Name_key():

    """Creates a list of names for the numeric patterns of the generate object"""

    def __init__(self,geo):
        self.dic_list = {}
        self.name_list = []
        self.key = "key.txt"
        self.geo = geo

    def load_key(self):

        """loads a text file containing the names and numeric values and saves it to a dict"""
        file = open(self.key)
        for line in file:
            x = line.strip().split(";")
            key =x[0]
            value = list(eval(x[1]))
            self.dic_list[key] = value
        file.close()

    def name_figure(self):

        """compares the numeric values of the figures against the keys and assigns a name to the figure and creates a list of names"""
        c= 0
        while c < 15:
            for v in self.dic_list:
                if self.dic_list[v] == self.geo[c]:
                    self.name_list.append(v)
                    break
            c += 1

    def _name_key(self):

        """execute name-key object"""

        self.load_key()
        self.name_figure()

