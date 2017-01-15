from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self,hl):
        super(Square,self).__init__(hl,hl)
        

s=Square(60)
