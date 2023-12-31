import numpy as np


class Intercept(object):
    def __init__(self, distance, point, normal, obj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.obj = obj



class Shape(object):

    def __init__(self, position, material):
        self.position = position
        self.material = material

    def ray_intersect(self, origin, direction):
        return None


class Sphere(Shape):

    def __init__(self, position, radius, material):
        self.radius = radius
        super().__init__(position, material)


    def ray_intersect(self, origin, direction):

        L = np.subtract(self.position, origin)
        lengthL = np.linalg.norm(L)
        tca = np.dot(L, direction)
        d = (lengthL**2 - tca **2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius **2 - d **4) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        P = np.add(origin, t0 * np.array(direction))
        point_normal = np.subtract(P, self.position)
        point_normal = point_normal / np.linalg.norm(point_normal)

        return Intercept(distance = t0,
                         point = P,
                         normal = point_normal,
                         obj = self)