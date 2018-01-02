#!/usr/bin/env python
#coding: utf-8


"""
Module representing a pupil.
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pybib.pupil import Pupil

from pybib.pupil import Pupil
from pybib.pupil_edit_ui import Ui_Dialog

class PupilEditDialog(QDialog, Ui_Dialog):

    def __init__(self, pupil=None):
        super(PupilEditDialog, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Setup slots and signals
        self.deleteButton.pressed.connect(self.delete_pupil)

        # Setup internals
        self.pupil = pupil or Pupil()
        self.populate()

    def populate(self):
        self.idEdit.setText(self.pupil.id)
        self.prenameEdit.setText(self.pupil.prename)
        self.nameEdit.setText(self.pupil.name)
        self.gradeEdit.setText(self.pupil.grade)

    def delete_pupil(self):
        self.pupil.delete()
