class Rectangle:
    def __init__(self, width, height):
        self.width, self.height = width, height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # return "Too big for picture." if self.width > 50 or self.height > 50 else ''.join(['*' * self.width + '\n' for row in range(self.height)])
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ''.join(['*' * self.width + '\n' for row in range(self.height)])

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = self.height = side

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height

