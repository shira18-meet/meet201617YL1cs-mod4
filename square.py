from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self,hl):
        super(Square,self).__init__(hl,hl)
    def set_length(self,hl):
        Square.set_height(hl)
        Square.set_length(hl)


s=Square(100)
s.draw_shape()

