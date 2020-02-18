# -*- coding: utf-8 -*-
"""
@author: 105502506
"""

import sys
from PyQt5 import QtWidgets
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.resize(600, 500)
    w.setWindowTitle("Risky Football Match Predictor")
    w.show()
