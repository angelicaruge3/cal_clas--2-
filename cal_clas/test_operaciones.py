import pytest
from operaciones import  area_cuadrado,area_circulo, area_triangulo, area_rectangulo, area_rombo, area_paralelogramo, area_pentagono, area_hexagono

def test_area_cuadrado():
    assert area_cuadrado(3) == 9
    assert area_cuadrado(2) == 4
"""
def test_area_circulo():
    assert area_circulo(4) == 50
"""

def area_triangulo():
    assert area_triangulo(2,6) == 12
    assert area_triangulo(3,9) == 2

def area_rectangulo():
    assert area_rectangulo(7,3) == 21
    assert area_rectangulo(8,2) == 16

def area_rombo():
    assert area_rombo(8,2) == 8
    assert area_rombo(7,4) == 14

def area_paralelogramo():
    assert area_paralelogramo(5,5) == 25
    assert area_paralelogramo(3,7) == 21

def area__pentagono():
    assert area__pentagono(2,3) == 15
    assert area__pentagono(8,3) == 60

def area_hexagono():
    assert area_hexagono(3,6) == 54
    assert area_hexagono(2,5) == 30