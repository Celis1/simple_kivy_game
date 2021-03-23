#- creating random functions that control the ints

class add_score():
    '''takes a score widget and adds points to the string'''
    def __init__(self,score_obj,points=1):
        self.score = score_obj
        self.text = self.score.text[0:self.score.text.find(' ')+1]
        self.score_int = self.score.text.find(' ')+1
        self.new_score = int(self.score.text[self.score_int:len(self.score.text)]) +10
        self.score.text = self.text +str(self.new_score)


class lose_life():
    '''call function to subtract 1 from life points #later will
    have images for life points'''
    def __init__(self,life_obj):
        self.life = life_obj
        self.text = self.life.text[0:self.life.text.find(' ')+1]
        self.life_int = self.life.text.find(' ')+1 #find includes the postion of the found str
        self.new_life_points = int(self.life.text[self.life_int:len(self.life.text)]) - 1
        self.life.text = self.text + str(self.new_life_points)
        self.check_num()
        #print(self.text)
    def check_num(self):
        if self.new_life_points == 0:
            print('NO LIVES BOIII')
