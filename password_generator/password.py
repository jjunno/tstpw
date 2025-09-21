import json
from os import listdir

class Password:
    def __init__(self, original):
        self.original = original
        self.filenames = ["firstnames_men_fi_avoindata.json", "firstnames_women_fi_avoindata.json", "surnames_fi_avoindata.json", "lang_fi_kotus.json"]
        self.ruleset = []
        self.words = []

        print(f"Original password is \"{original}\"")
        self.read_files()

    def read_files(self):
        for filename in self.filenames:
                file = open(f"wordlists_json/{filename}", "r", encoding="utf-8")
                content = json.load(file)
                for line in content:
                    self.words.append(line)
                
        print(f"{len(self.filenames)} files read, total {len(self.words)} words found")

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

    # Does original password exist in words as it is
    def is_in_lists(self):
        for word in self.words:
            if word == self.original:
                return True
        return False