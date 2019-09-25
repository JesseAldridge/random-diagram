import os, json, random
from pathlib import Path


def weighted_choice(choices):

    # Return weighted random selection; format: {'choice1':.7, 'choice2':.5}

    if not choices:
        raise IndexError  # raise IndexError on empty dict
    total = sum(choices.values())
    rand = random.uniform(0, total)
    upto = 0
    for choice, weight in choices.items():
        if upto + weight > rand:
            return choice
        upto += weight

paths = []
for path in Path(os.path.expanduser('~/Dropbox/diagrams/')).glob('**/*.drawio'):
  paths.append(str(path))

path_to_score = {}
meta_path = os.path.expanduser('~/Dropbox/random-diagram/path-meta.json')
if os.path.exists(meta_path):
  with open(meta_path) as f:
    json_text = f.read()
  try:
    path_to_score = json.loads(json_text)
  except json.decoder.JSONDecodeError:
    pass

for path in paths:
  if path not in path_to_score:
    path_to_score[path] = 1.0

json_out = json.dumps(path_to_score, indent=2)
with open(meta_path, 'w') as f:
  f.write(json_out)

print(weighted_choice(path_to_score))
