from bs4 import Beautifulsoup
import request
import requests.exceptions
import urllib.parse
from collections import deque
import re

usr_url = str(input('[+]Enter User URL To Scan[+]'))
urls = deque([user_url])
