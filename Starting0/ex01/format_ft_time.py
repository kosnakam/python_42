import time
from datetime import datetime

seconds = time.time()
now = datetime.now()

# com_seconds = "{:,.4f}".format(seconds)
# sci_seconds = "{:.2e}".format(seconds)
com_seconds = f"{seconds:,.4f}"
sci_seconds = f"{seconds:.2e}"
date = now.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", com_seconds, "or", sci_seconds, "in scientific notation")
print(date)