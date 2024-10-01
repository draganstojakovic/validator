import datetime as dt

import json

file = {
    "date": (dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=5000)).isoformat(),
    "validate": True,
}

with open("datetime.json", "w", encoding="UTF-8") as f:
    json.dump(file, f, indent=2)
