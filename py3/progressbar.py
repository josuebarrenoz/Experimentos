import time
def progress_bar(part, total, length =30):
    frac = part/total
    completed = int(frac*length)
    missing = length - completed
    bar = f"[{'#'*completed}{'-'*missing}]{frac:.2%}"
    return bar

n = 30

for i in range (n+1):
    time.sleep(0.1)
    print(progress_bar(i,n), end='\r')
