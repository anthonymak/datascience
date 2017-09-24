Description

This Python module can be used for generating sample data for machine learning testing.
To use, updates your features and create your model. See the sample files for example:
- features/features.json
- weather_model.py
- GenerateWeather.py

The features.json file is used to generate the columns in the data file. You can generate columns with string, float, and datetime types currently.
In order to create the Y-labels for each role, you will need to supply your own model definition which implements the IModel abstract class.

To install:

sudo python setup.py install

To run:

python GenerateWeather.py

Output:

Output can be found in the output directory "/output"