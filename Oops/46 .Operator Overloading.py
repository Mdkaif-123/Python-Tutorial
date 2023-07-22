
# ? Operator overloading is the process of  assigning a  specific task to the operator

class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self) -> str:
        return (f"{self.x}i + {self.y}y + {self.z}z")

    def __add__(self, x):
        return Vector(self.x + x.x , self.y +x.y , self.z + x.z)

    def __sub__(self, x):
        return Vector(self.x - x.x , self.y -x.y , self.z - x.z)
v1 = Vector(1,3,6)
print(v1)

v2 = Vector(2,3,5)
print(v2)

print(v1+v2)
print(v1-v2)