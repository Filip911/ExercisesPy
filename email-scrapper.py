from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
#pip3 install requests
#pip3 install bs4



usr_url = str(input('[+]Enter User URL To Scan[+]'))
urls = deque([user_url])
