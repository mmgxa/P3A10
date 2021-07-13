import math


##################################################
###########       The Polygon Class    ###########
##################################################
class Polygon:
    '''
    A Polygon Class which is intitialized with number of edges and its circumradius.

    Its properties such as interior angle, edge lengths, apothem, area, and perimeter are calculated,
    and can be accessed as key (p['n_edge']) or as property (p.n_edge).

    The former will give a soft warning and continue for a wrong key; the latter will halt if 
    the incorrect property is asked.
    '''

    def __init__(self, n_edge: int, circumradius: int) -> None:

        if n_edge < 3:
            raise ValueError(
                'The number of edges must be atleast 3 for a Polygon!')

        if circumradius < 0:
            raise ValueError(
                'The circumradius of a Polygon cannot be negative!')

        self.n_edge_i = n_edge
        self.circumradius_i = circumradius

    @property
    def n_edge(self) -> int:
        return self.n_edge_i

    @property
    def circumradius(self) -> int:
        return self.circumradius_i

    @property
    def int_angle(self) -> float:
        return (self.n_edge - 2)*(180/self.n_edge)

    @property
    def edgelen(self) -> float:
        return round(2*self.circumradius*math.sin(math.pi/self.n_edge), 2)

    @property
    def apothem(self) -> float:
        return round(self.circumradius * math.cos(math.pi/self.n_edge), 2)

    @property
    def area(self) -> float:
        return round(0.5*self.n_edge * self.edgelen * self.apothem, 2)

    @property
    def perimeter(self) -> float:
        return round(self.n_edge * self.edgelen, 2)

    def __getitem__(self, str):
        '''
        What to return when the properties of the object is passed as key 
        '''
        try:
            print(getattr(self, str))
        except AttributeError:
            print(
                'Key must be one of these: n_edge/circumradius/int_angle/edgelen/apothem/area/perimeter')

    def __repr__(self) -> str:
        '''
        How the output appears when the object is printed.
        '''
        return (f'Polygon Object with the following properties:' + f'\n'
                f'\t' + f'{self.n_edge} sides,' + f'\n'
                f'\t' + f'circumradius = {self.circumradius},' + f'\n'
                f'\t' + f'Interior Angle : {self.int_angle},' + f'\n'
                f'\t' + f'Edge Length : {self.edgelen},' + f'\n'
                f'\t' + f'Apothem : {self.apothem},' + f'\n'
                f'\t' + f'Area : {self.area},' + f'\n'
                f'\t' + f'Perimeter : {self.perimeter}')

    def __eq__(self, other):
        '''
        This compares two objects based on the Polygon Class based on their
        number of edges and circumradius ...
        '''
        if not isinstance(other, Polygon):
            raise TypeError(
                f'Second argument: Expected {type(self)} ; Found {type(other)}')
        return (self.n_edge == other.n_edge) and (self.circumradius == other.circumradius)

    def __gt__(self, other):
        '''
        This compares two objects based on the Polygon Class based on their
        number of edges only!
        '''
        if not isinstance(other, Polygon):
            raise TypeError(
                f'Second argument: Expected {type(self)} ; Found {type(other)}')
        return self.n_edge > other.n_edge


##################################################
#########       The Polygon Sequence    ##########
##################################################

class PolySeq():
    def __init__(self, max_edges: int, common_circumradius: int):

        if max_edges < 3:
            raise ValueError(
                'The maximum number of edges must be atleast 3 for any Polygon!')

        if common_circumradius <= 0:
            raise ValueError(
                'The common circumradius of a Polygon cannot be negative!')

        self.max_edges = max_edges
        self.common_circumradius = common_circumradius

        self.polygons = []
        self.polygons_area_perim = []
        for i in range(3, max_edges + 1):  # +1 to make it inclusive!
            p = Polygon(i, common_circumradius)
            self.polygons.append(p)
            self.polygons_area_perim.append(p.area / p.perimeter)

    def __len__(self):
        return len(self.polygons)



    def __getitem__(self, item):
        '''
        What to return when the properties of the object is passed as key 
        '''
        if item <= len(self.polygons) - 1:
            return self.polygons[item]
        else:
            raise ValueError('CustomPolygon: incorrect index of item')

    def __repr__(self) -> str:
        '''
        How the output appears when the object is printed.
        '''
        return (f'This Polygon Sequence contains polygons with the following properties:' + f'\n'
                f'\t' + f'Sides: From 3 to {self.max_edges},' + f'\n'
                f'\t' + f'Common circumradius = {self.common_circumradius},')

    @property
    def max_effic(self):
        return self.polygons[self.polygons_area_perim.index(max(self.polygons_area_perim))]