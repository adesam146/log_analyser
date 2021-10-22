from datetime import datetime, timedelta
from random import randint

with open('dummy.log', 'w') as file:
    startTime = datetime(2021, 10, 22)
    for i in range(12):
        time = startTime + timedelta(minutes=i)
        file.write(f'{time} [INF] ')

        if randint(0, 1) == 0:
            file.write('kjdhnaksdnajdnakjd')
        else:
            file.write('Hello')
        
        file.write('\n')
