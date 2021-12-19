
import sys
import os
import os.path
import time
import shutil
from subprocess import Popen, PIPE
from datetime import datetime

while True:
  process = Popen(['./fscm', '0.0.0.0', '8864', 'guswns'])
  process.wait()