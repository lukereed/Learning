"""
Homework for 1/6/2016

Create a python script which will calculate the
wind speed at a specified height with the inputs:
1.) Measurement Height 1 (MH1)
2.) Wind speed at measurement height 1 (WS1)
3.) Measurement Height 2 (MH2)
4.) Wind speed at measurement height 2 (WS2)
5.) Height at which you want the wind speed (DH)

Use sys.argv so that the script can be run in the
following manner:
$ python PythonHomework1.py MH1 WS1 MH2 WS2 DH

Which will end up printing:
$ The wind speed at 80m is 9.8m/s

The calculation should be inside a function/method.

For those not in the wind group, the calculation
is as follows:
shear_exponent = ln(WS1 / WS2) / ln(MH1 / MH2)
wind_speed = WS2 * (DH / MH2) ^ shear_exponent

"""

