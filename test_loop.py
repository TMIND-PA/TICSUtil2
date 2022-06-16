from TICSUtil2 import TICSLogger
import time

# Log = TICSLogger(dir="./logs", msg_col_len=90, rotation="17:51").get_log()
Log = TICSLogger(dir="./logs", msg_col_len=90, rotation="1 KB").get_log()


for i in range(8):
    Log.info(f"{i}: Sample INFO message")
    time.sleep(1)
