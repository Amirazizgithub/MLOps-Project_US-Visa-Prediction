# Path: demo.py
import sys
from US_Visa_Prediction.logger import logging
from US_Visa_Prediction.exceptions import USvisaException


logging.info("Welcome to our custom log")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)