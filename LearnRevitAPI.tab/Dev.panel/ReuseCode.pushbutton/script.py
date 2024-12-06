# -*- coding: utf-8 -*-
__title__ = "Reuse Code in pyRevit"
__doc__ = """Version = 1.0
Date    = 05.12.2024----
_____________________________________________________________________
Description:
Learn how to create reusable code with pyRevit.
_____________________________________________________________________
Author: Rajkumar Kolli"""

from sys import prefix

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==================================================
from Autodesk.Revit.DB import *


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==================================================
from Autodesk.Revit.UI import UIDocument
#from unicodedata import category

#from lib.Samples.FilteredElementCollector import collector

doc   = __revit__.ActiveUIDocument.Document #type : Document
uidoc = __revit__.ActiveUIDocument          #type : UIDocument
app   = __revit__.Application               #type : Application

#1️⃣Use ofcalss method to apply an elementclassfilter and find levels in the document

collector = FilteredElementCollector(doc)
levels    = collector.OfClass(Level).ToElements()

for lvl in levels:
    print(lvl,lvl.Name)