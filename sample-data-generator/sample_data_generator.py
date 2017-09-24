import random
import numpy as np
import datetime
import logging
import sys
import time



# This class can be used to generate a variety of sample data based on user-defined features and user-defined model
class SampleDataGenerator:

    def __init__(self, featuresDefinition, model, outputFile, delimeter= "|"):
        self.model = model
        self.featuresDefinition = featuresDefinition
        self.delimeter = delimeter
        self.outputFile = outputFile
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    def __generateOneColumn(self, colDef):
        if colDef['Type'] == "str":
            strings = colDef["Values"]
            return random.choice(strings)
        elif colDef['Type'] == "float":
            return str(np.random.normal(colDef['Values']['Mean'], colDef['Values']['Std'], 1)[0])
        elif colDef['Type'] == "datetime":
          startDate = datetime.datetime.strptime(colDef['Values']['StartDate'], "%Y-%m-%dT%H:%M:%SZ")
          timedelta = datetime.timedelta(milliseconds=colDef['Values']['IntervalMS']) * self.i
          return (startDate + timedelta).strftime("%Y-%m-%dT%H:%M:%SZ")
        elif colDef['Type'] == "label":
          return "label"
        else:
            return "UNDEFINED"

    def __genOneRow(self):
        row = []
        for i in range(len(self.featuresDefinition)):
            row.append(self.__generateOneColumn(self.featuresDefinition[i]))
        label = self.model.transform(row)
        row.append(label)
        return self.delimeter.join(row)

    # Generate sample data. Specify number of rows to generate. Data will be generated in a directory specified.
    def generateSampleData(self, numOfRows):
      start = time.time()

      for i in range(numOfRows):
            self.i = i
            row = self.__genOneRow()
            logging.debug(row)
            self.outputFile.write(row + '\n')

      end = time.time()
      logging.debug('Took %f seconds to generate %d rows' % ((end - start), numOfRows))  # TODO print time to run

