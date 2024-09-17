# importing the necessary dependencies
import numpy as np
import pandas as pd
from transformers import pipeline
from nltk.tokenize import sent_tokenize

# importing the date and time module
from datetime import datetime

pip install -U -q google-generativeai
# import necessary modules.
import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
from IPython.display import Markdown
# setting API key
from kaggle_secrets import UserSecretsClient

# installing simpful library
!pip install simpful
# import dependencies
import random as rn
from simpful import *
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")