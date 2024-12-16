import json
import time

data = {
  "cache_size": 1,
  "items": {
    "myrealkey": {
      "data": "TestData",
      "timestamp": int(time.time())
    }
  }
}

print(json.dumps(data, indent=2))
