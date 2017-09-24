import abc

# Implement this interface to supply your own model.
# This model is used to generate the label values
class IModel(metaclass=abc.ABCMeta):

    # fuzzingRatio is to randomize label values (Y). For example to specify 5% fuzzing set fuzzingRatio to 0.05
    def __init__(self, fuzzingRatio = 0.0):
      self.fuzzingRatio = fuzzingRatio

    @abc.abstractmethod
    def transform(self, featuresArray):
        pass