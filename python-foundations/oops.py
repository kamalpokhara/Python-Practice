class Shape:
    """Class to represent a shape. \n
    attributes: \n
        length: Length of shape \n
        breadth: breadth of shape \n
    """

    Count = 0

    def __init__(self, l=None, b=None):
        if not l or not b:
            self.length = int(input("Enter length "))
            self.breadth = int(input("Enter breadth "))
        else:
            self.length = l
            self.breadth = b

        Shape.Count += 1
        print("Shaper has been initilazed ")
        print("Total Shape: ", Shape.Count)

    def __del__(self):
        print("Shape has been deleted")
        Shape.Count -= 1
        print("Total shaper: ", Shape.Count)

    @property
    def area(self):

        print("area is  ", self.length * self.breadth)

    @property
    def perimeter(self):
        print("Perimeter is x ", (self.length + self.breadth) * 2)


shp = Shape()
shp.length
shp.area
shp.perimeter

del shp

shp2 = Shape()
shp2.length
shp2.area
shp2.perimeter
