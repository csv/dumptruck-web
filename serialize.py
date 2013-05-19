import json
import csv
import StringIO

def csvdump(data):
    'Dump a list of dictionaries to CSV.'
    print json.dumps(data)
    if len(data) == 0:
        # It would be nice if this had the header row or raised an error or something.
        return '\n'
    else:
        keys = data[0].keys()
        output = StringIO.StringIO()
        c = csv.DictWriter(output, keys)
        c.writer.writerow(keys)
        c.writerows(data)
        return output.getvalue()

SERIALIZATIONS = {
    'json': json.dumps,
    'csv': csvdump
}

