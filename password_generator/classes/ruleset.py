import json
from os import listdir

class Ruleset:
    def __init__(self):
        self.ruleset = []
        self.read_rulesets()

    # Read all .json files in rulesets directory.
    def read_rulesets(self):
        filenames = []
        for i in listdir("rulesets"):
            if i.endswith(".json"):
                filenames.append(i)

        for filename in filenames:
                file = open(f"rulesets/{filename}", "r", encoding="utf-8")
                content = json.load(file)
                for line in content:
                    self.ruleset.append(line)
                
        print(f"{len(filenames)} ruleset files read, total {len(self.ruleset)} rules found")

    def run_all_in_order(self):
         print("Running all rulesets in order")