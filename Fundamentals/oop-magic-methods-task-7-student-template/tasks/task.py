from datetime import datetime
import time
from contextlib import ContextDecorator


class LogFile(ContextDecorator):
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dat_time = datetime.now()
        self.exc_time = self.dat_time - self.start_time
        with open(self.log_file, 'a') as log_f:
            my_str = f'Start: {self.dat_time} | Run: {self.exc_time} | An error occurred: {exc_val}\n'
            log_f.write(my_str)
        return False


@LogFile('my_trace.log')
def some_func():
    print('a mama baba')
    time.sleep(2)



some_func()