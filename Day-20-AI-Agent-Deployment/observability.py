# Implement logging, timeout, and retry

# retry and timeout in main.py

# Logging
import logging
import time
from collections import defaultdict, deque


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("ai_agent")

#  check for rate limit
REQUEST_LIMIT = 10
WINDOW_SECONDS = 60

request_times = defaultdict(deque)

def check_rate_limit(client_id: str) -> bool:
    now = time.time()
    times = request_times[client_id]
    while times and now - times[0] > WINDOW_SECONDS:
        times.popleft()
    if len(times) >= REQUEST_LIMIT:
        return False
    times.append(now)
    return True

