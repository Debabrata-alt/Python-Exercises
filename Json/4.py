# Write a Python program to create a new JSON file from an existing JSON file.

import json

all_states = {
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "code": 120
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "code": 121
    },
    {
      "name": "Arizona",
      "abbreviation": "AZ",
      "code": 122
    },
    {
      "name": "Arkansas",
      "abbreviation": "AR",
      "code": 123
    },
  ]
}

for state in all_states["states"]:
  del state["code"]

all_states_json = json.dumps(all_states, indent = 2)

print(all_states_json)

'''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL"
    },
    {
      "name": "Alaska",
      "abbreviation": "AK"
    },
    {
      "name": "Arizona",
      "abbreviation": "AZ"
    },
    {
      "name": "Arkansas",
      "abbreviation": "AR"
    }
  ]
}
'''