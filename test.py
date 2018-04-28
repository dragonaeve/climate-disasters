import femaapi as fema
import json

disasters = ["'Human Cause'", "'Chemical'"]

results = fema.filterByType(disasters)

from_date = "1980-01-02"
to_date = "2012-01-05"

results2 = fema.filterByDate(from_date, to_date)

results3 = fema.filterDateType(from_date, to_date, disasters)

print(json.dumps(results3, indent=4, sort_keys=True))