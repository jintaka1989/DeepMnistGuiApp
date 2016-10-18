# -*- coding: utf-8 -*-
from PyQt4 import uic

fin = open('deep_mnist.ui', 'r')
fout = open('deep_mnist.py', 'w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()
