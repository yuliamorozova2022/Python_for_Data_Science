
# import time
# print("Seconds since January 1, 1970:", time.time())

import time

from datetime import datetime

# Print the Unix timestamp in scientific notation
timestamp = time.time()
# print(timestamp)
# start_date = datetime(1970, 1, 1)
# target_date = datetime(timestamp)

# # Calculate the difference in seconds
# difference_in_seconds = (target_date - start_date).total_seconds()
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

# Print the formatted date
formatted_date = time.strftime("%b %d %Y", time.gmtime(timestamp))
print(formatted_date)
