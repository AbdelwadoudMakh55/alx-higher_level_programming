#!/usr/bin/python3
""" This is the square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        sq_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return f"{sq_str}"
