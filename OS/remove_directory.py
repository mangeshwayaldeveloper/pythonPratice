import os
try:
    os.remove('data')
except Exception as e:
    print(e)