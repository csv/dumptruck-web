import json
import csv
import StringIO

def csvdump(data):
    'Dump a list of dictionaries to CSV.'
    keys = data.keys()
    output = StringIO.StringIO()
    c = csv.DictWriter(f, keys)
    c.writer.writerow(keys)
    c.writerows(data)
    return output.getvalue()

SERIALIZATIONS = {
    'json': json.dumps,
    'csv': csvdump
}

