# Session 10 Readme file.

### Only the major code segments are shown


## Q1. Create a Polygon Class...


The polygon class takes two arguments in its initializer

```python
def __init__(self, n_edge: int, circumradius: int) -> None:
```

The attributes required in the assignment are defined as properties

```python
@property
def int_angle(self) -> float:
	return (self.n_edge - 2)*(180/self.n_edge)
```


The `__get__item` function is also defined

```python
def __getitem__(self, str):
	'''
	What to return when the properties of the object is passed as key 
	'''
	try:
		print(getattr(self, str))
	except AttributeError:
		print(
			'Key must be one of these: n_edge/circumradius/int_angle/edgelen/apothem/area/perimeter')
```

The ``__repr__`` function is defined 

```python
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
```

The equality operation is defined using the ``__eq__`` function. It checks for both the number of edges and the circumradius

```python
def __eq__(self, other):
	'''
	This compares two objects based on the Polygon Class based on their
	number of edges and circumradius ...
	'''
	if not isinstance(other, Polygon):
		raise TypeError(
			f'Second argument: Expected {type(self)} ; Found {type(other)}')
	return (self.n_edge == other.n_edge) and (self.circumradius == other.circumradius)
```


The greather than operation is defined using the ``__gt__`` function. It checks for using only the number of edges 

```python
def __gt__(self, other):
	'''
	This compares two objects based on the Polygon Class based on their
	number of edges only!
	'''
	if not isinstance(other, Polygon):
		raise TypeError(
			f'Second argument: Expected {type(self)} ; Found {type(other)}')
	return self.n_edge > other.n_edge
```




## Q2. Implement a Custom Polygon sequence type...

The polygon sequence takes two arguments in its initializer

```python
def __init__(self, max_edges: int, common_circumradius: int):
```

In the initializer, the list of polygons along with their area-to-perimeter ratio is created

```python
self.polygons = []
self.polygons_area_perim = []
for i in range(3, max_edges + 1):  # +1 to make it inclusive!
	p = Polygon(i, common_circumradius)
	self.polygons.append(p)
	self.polygons_area_perim.append(p.area / p.perimeter)
```

The ``__len__`` function is also defined and returns the number of polygons in the list

```python
def __len__(self):
	return len(self.polygons)
```

The `__get__item` function is also defined

```python
def __getitem__(self, item):
	'''
	What to return when the properties of the object is passed as key 
	'''
	if item <= len(self.polygons) - 1:
		return self.polygons[item]
	else:
		raise ValueError('CustomPolygon: incorrect index of item')
```

The ``__repr__`` function is defined 

```python
def __repr__(self) -> str:
	'''
	How the output appears when the object is printed.
	'''
	return (f'This Polygon Sequence contains polygons with the following properties:' + f'\n'
			f'\t' + f'Sides: From 3 to {self.max_edges},' + f'\n'
			f'\t' + f'Common circumradius = {self.common_circumradius},')
```

Finally, the maximum efficiency function property is defined

```python
@property
def max_effic(self):
	return self.polygons[self.polygons_area_perim.index(max(self.polygons_area_perim))
```
