#!/usr/bin/python
import sys
import pytest
import glob

try:
    from pylint.lint import Run as RunPylint
except ImportError as exc:
    print("Pylint no disponible")

try:
    import pycodestyle
except ImportError as exc:
    print("PyCodeStyle no disponible")

"""
Pueden utilizar este script para ejecutar los tests dentro de Thonny.
(ejecutenló como otro programa)
"""


def generador_bloque(mensaje, ancho=80):
    print("~" * 10)
    print(mensaje)
    print("~" * 10)


def do_pytest():
    generador_bloque("Comenzando tests")
    pytest.main()


def do_pylint():
    generador_bloque("Ejecutando Pylint")
    sources = list(glob.glob("src/practica/*.py"))
    tests = list(glob.glob("tests/*.py"))
    archivos = sources + tests
    RunPylint(archivos)


def do_codestyle():
    generador_bloque("Ejecutando codestyle")
    style = pycodestyle.StyleGuide()
    style.input_dir(".")


if __name__ == "__main__":
    sys.path.append("src")
    do_pytest()
    do_codestyle()
    do_pylint()
