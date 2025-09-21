import json
from classes.ruleset import Ruleset

class Password:
    def __init__(self, original):
        self.original = original
        self.filenames = ["firstnames_men_fi_avoindata.json", "firstnames_women_fi_avoindata.json", "surnames_fi_avoindata.json", "lang_fi_kotus.json"]
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

    # Does original password exist in words as it is
    def is_in_lists(self):
        for word in self.words:
            if word == self.original:
                return True
        return False
    
    def apply_ruleset(self):
        r = Ruleset(self)
        if r.prepend_ruleset():
              return True
        if r.append_ruleset():
              return True
        if r.try_upper_case():
              return True
        return False