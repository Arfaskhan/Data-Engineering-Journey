import time
from datetime import datetime


an = 0
if an == 1:

    with open('Write_log.txt', 'a') as file:
        file.write(f"{datetime.now()}\n")

# Scheduluing using While
an = 0
if an == 1:


    def time_print():
        with open('Time_print.txt', 'a') as file:
            file.write(f"Run script at {datetime.now()}\n")


    while True:
        time_print()
        time.sleep(10)