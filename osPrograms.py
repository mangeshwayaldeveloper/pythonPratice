import os
import sys
def check_reboot():
 """Returns true"""
 return os.path.exists("/run/reboot-required")

 def main():
   if check_reboot():
    print("pending reboot")
    sys.exit(1)

 main()