# This source code is a part of Project Violet.
# Copyright (C) 2021. violet-team. Licensed under the Apache-2.0 License.

import sys
import os
from os import listdir
import os.path
from os.path import isfile, join
import re

sched_slot_count = 20

if os.path.exists('workspace/lock-' + sys.argv[1]):
    exit(-1)

open('workspace/lock-' + sys.argv[1], 'w').close()