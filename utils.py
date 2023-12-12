import csv
from tqdm import tqdm

# -----------------------------------------------------------------------------
def countColumnValues(filename, columnName):

  numberRows = 0
  with open(filename, 'r') as countFile:
    numberRows = sum(1 for line in countFile)

  with open(filename, 'r') as inFile:
    inputReader = csv.DictReader(inFile)

    if columnName not in inputReader.fieldnames:
      raise Exception(f'Error: column {columnName} not in file {filename}')

    data = {}
    for row in tqdm(inputReader, total=numberRows):
      value = row[columnName] 
      if value not in data:
        data[value] = 0
      else:
        data[value] += 1

    return data

# -----------------------------------------------------------------------------
def readColumnData(filename, groupColumns, columnNames):

  numberRows = 0
  with open(filename, 'r') as countFile:
    numberRows = sum(1 for line in countFile)

  with open(filename, 'r') as inFile:
    inputReader = csv.DictReader(inFile)

    for col in groupColumns + columnNames:
      if col not in inputReader.fieldnames:
        raise Exception(f'Error: column {col} not in file {filename}')

    data = {}
    for row in tqdm(inputReader, total=numberRows):
      groupIDValues = [row[x] for x in groupColumns]
      groupID = ' '.join(groupIDValues)
      if groupID not in data:
        data[groupID] = {}
      for col in columnNames:
        value = row[col]
        if col in data[groupID]:
          if value in data[groupID][col]:
            data[groupID][col][value] += 1
          else:
            data[groupID][col][value] = 1
        else:
          data[groupID][col] = {value: 1}

    return data
