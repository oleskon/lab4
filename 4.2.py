

import json

def task(file_name):
    with open(file_name) as fh:
        return sum([d['score'] * d['weight'] for d in json.load(fh)])

print("%.3f" % task('input.json'))