from session10 import *
import pytest


##########################################
###########  Polygon Class  ##############
##########################################
def test_class_repr():
    '''
    Check for the __repr__ function for the Polygon Class
    '''
    pol = Polygon(3, 3)
    assert str(pol), "Your repr function is missing"


def test_class_eq():
    '''
    Check whether two same Polygons are deemed Equal
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(3, 3)
    assert pol1 == pol2, 'Your equality function is bogus'


def test_class_neq():
    '''
    Check whether two same Polygons are deemed Equal
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(4, 3)
    assert pol1 != pol2, 'Your equality function is bogus'


def test_class_gr():
    '''
    Check if one Polygon is greather than other
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(4, 3)
    assert pol1 < pol2, 'Your greater function is bogus'


def test_class_ngr():
    '''
    Check if one Polygon is greather than other
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(4, 3)
    assert (pol1 > pol2) == False, 'Your greater function is bogus'


def test_class_prop():
    '''
    Check for the existence of the properties mentioned in the assignment
    '''
    pol = Polygon(3, 3)
    for prop in ['n_edge', 'circumradius', 'int_angle', 'edgelen', 'apothem', 'area', 'perimeter']:
        assert getattr(
            pol, prop), 'At least one of the required attributes is missing!'


##########################################
##########  Polygon Sequence  ############
##########################################
def test_seq_repr():
    '''
    Check for the __repr__ function for the Polygon Sequence
    '''
    polseq = PolySeq(3, 3)
    assert str(polseq), "Your repr function is missing"


def test_seq_len():
    '''
    Check for the __len__ function for the Polygon Sequence
    '''
    polseq = PolySeq(3, 3)
    assert len(polseq), "Your len function is missing"


def test_seq_get():
    '''
    Check for the __getitem__ function for the Polygon Sequence
    '''
    polseq = PolySeq(3, 3)
    assert polseq[0], "Your len function is missing"


def test_seq_prop():
    '''
    Check for the existence of the properties mentioned in the assignment
    '''
    polseq = PolySeq(3, 3)
    assert getattr(
        polseq, 'max_effic'), 'The maximum efficiency property is missing!'
