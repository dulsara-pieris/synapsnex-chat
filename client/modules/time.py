from datetime import datetime
from platformdirs import user_config_dir
import os

cfg = user_config_dir("synapsnex")
os.makedirs(cfg, exist_ok=True)

log = os.path.join(cfg, "login.log")

def save_login():
              try:
                            with open(log, "r") as f:
                                          lgs = f.readlines()
              except FileNotFoundError:
                            lgs = []

              lgs.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
              lgs = lgs[:3]  
              with open(log, "w") as f:
                            f.writelines(lgs)
                            
def last():
              try:
                            with open(log, "r") as f:
                                          lgs = f.readlines()
              except FileNotFoundError:
                            print("NO LOGIN DATA FOUND")
                            return

              print("LAST LOGIN:")
              for l in lgs:
                            print("-", l.strip())
