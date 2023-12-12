import unittest
import tempfile
import csv
import os
import utils

# Don't show the traceback of an AssertionError, because the AssertionError already says what the issue is!
__unittest = True

# -----------------------------------------------------------------------------
def getNumberOfRows(filename):
  with open(filename, 'r') as inFile:
    return sum(1 for l in inFile)

# -----------------------------------------------------------------------------
def getColumnValues(filename, columnName):
  with open(filename, 'r') as inFile:
    reader = csv.DictReader(inFile, delimiter=',')
    return sorted({s[columnName] for s in reader})


# -----------------------------------------------------------------------------
class TestUtils(unittest.TestCase):

  # ---------------------------------------------------------------------------
  def setUp(self):
    self.outputFile = os.path.join(tempfile.gettempdir(), 'computed-diff.csv')

  # ---------------------------------------------------------------------------
  def tearDown(self):
    if os.path.isfile(self.outputFile):
      os.remove(self.outputFile)

  # ---------------------------------------------------------------------------
  def testReadColumnDataMissingGroupColumnWarning(self):
    """When one of the columns that should be used as a group key is missing, an error should be thrown"""
    with self.assertRaises(Exception):
      utils.readColumnData('./test/resources/example-rows.csv', ['column-not-exists'], ['BrutoBPM'])
    
  # ---------------------------------------------------------------------------
  def testReadColumnDataMissingColumnWarning(self): 
    """When one of the value columns is missing, an error should be thrown"""
    with self.assertRaises(Exception):
      utils.readColumnData('./test/resources/example-rows.csv', ['Merk'], ['not-exists'])

  # ---------------------------------------------------------------------------
  def testReadColumnDataGroup1Column(self):
    """When using one group key, counting should work."""
    data = utils.readColumnData('./test/resources/example-rows.csv', ['Merk'], ['Aantal zitplaatsen'])
    expectedData = {'RENAULT': {'Aantal zitplaatsen': {'3': 1, '2': 1}}, 'FORD': {'Aantal zitplaatsen': {'': 1}}, 'VOLKSWAGEN': {'Aantal zitplaatsen': {'3': 1}}}
    self.assertEqual(data, expectedData, msg='Single column group did not work')
 
  # ---------------------------------------------------------------------------
  def testReadColumnDataGroupMultipleColumns(self):
    """When using several group key, counting should work."""
    data = utils.readColumnData('./test/resources/example-rows.csv', ['Merk', 'Handelsbenaming'], ['Aantal zitplaatsen'])
    expectedData = {'RENAULT MASTER 2.8T L1H1 2.5 DCI 100': {'Aantal zitplaatsen': {'3': 1}}, 'FORD TRANSIT CONNECT 220L HR VAN 1.8TD 55': {'Aantal zitplaatsen': {'': 1}}, 'VOLKSWAGEN TRANSPORTER BESTEL TDI 96KW 1.0': {'Aantal zitplaatsen': {'3': 1}}, 'RENAULT KANGOO 1.5 DCI 80 EURO 2000': {'Aantal zitplaatsen': {'2': 1}}}
    self.assertEqual(data, expectedData, msg='Multiple column group did not work')
 
  # ---------------------------------------------------------------------------
  def testReadColumnDataGroup1Column(self):
    """Counting values of several columns should work."""
    data = utils.readColumnData('./test/resources/example-rows.csv', ['Merk'], ['Aantal zitplaatsen', 'Aantal cilinders'])
    expectedData = {'RENAULT': {'Aantal zitplaatsen': {'3': 1, '2': 1}, 'Aantal cilinders': {'4': 2}}, 'FORD': {'Aantal zitplaatsen': {'': 1}, 'Aantal cilinders': {'4': 1}}, 'VOLKSWAGEN': {'Aantal zitplaatsen': {'3': 1}, 'Aantal cilinders': {'5': 1}}}

    self.assertEqual(data, expectedData, msg='Counting values of several columns did not work')
 
