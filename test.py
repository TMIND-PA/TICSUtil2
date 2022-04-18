from TICSUtil2 import TICSLogger, emoji

# New Method
Log = TICSLogger(dir="./logs", msg_col_len=120).get_log()
Log.info(f"Logger Configured...")
Log.log(50, f"Sample LOG message")
Log.debug(f"Sample DEBUG message")
Log.info(f"Sample INFO message")
Log.warning(f"Sample WARNING message")
Log.error(f"Sample ERROR message")
Log.critical(f"Sample CRITICAL message")
Log.info(emoji["namaste"])


@Log.catch()
def exception_log():
    try:
        x = 1
        y = 0
        a = x / y
    except Exception as e:
        Log.exception(f"Sample EXCEPTION message with traceback. Error: {e}")


# Exception logging
exception_log()

# Logging from classes
class TestClass:
    def __init__(self):
        Log.info(f"TestClass Initialized")

    def test_func(self):
        Log.info(f"Inside Test Func")


test1 = TestClass()
test1.test_func()
