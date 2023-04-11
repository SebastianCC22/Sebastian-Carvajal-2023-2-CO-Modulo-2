# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Dino Runner",
    version="1.0",
    description="Juego Dino Runner de Chrome",
    author="SebitasCC22",
    author_email="Sebastian.c.c1418@gmail.com",
    url="https://github.com/SebastianCC22/Sebastian-Carvajal-2023-2-CO-Modulo-2",
    scripts=["main.py"],
    console=["main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)