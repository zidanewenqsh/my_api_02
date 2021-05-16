import os
import sys
import time
r,w = os.pipe()
fd = os.fdopen(w, 'w')