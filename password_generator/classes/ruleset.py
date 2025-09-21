import json
from os import listdir
from datetime import datetime

class Ruleset:
    def __init__(self, password):
        self.password = password
        self.ruleset = []
        self.read_rulesets()
        
        # Actual character, list of leet characters
        self.leet_dict = {
             "a": ["@", "4"],
             "b": ["8", "3", "13"],
             "e": ["3"],
             "g": ["6"],
             "o": ["0"],
             "i": ["1", "!"],
             "s": ["5", "$"],
             "t": ["7"],
             "x": ["x"],
             "x": ["x"],
             "x": ["x"],
        }

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

    def prepend_ruleset(self):
        print("Prepending ruleset")
        for word in self.password.words:
              for rule in self.ruleset:
                   w = word + rule
                   if w == self.password.original:
                        return True
        return False

    def append_ruleset(self):
        print("Appending ruleset")
        for word in self.password.words:
              for rule in self.ruleset:
                   w = rule + word
                   if w == self.password.original:
                        return True
        return False

    def try_upper_case(self):
        print("Trying upper case")
        for word in self.password.words:
             # No need to try lowering as all materila is lower
             if word.upper() == self.password.original:
                  return True
        return False

    # Iterate each character of each word.
    # Apple, aPple, apPle, etc.
    def try_char_capitalization(self):
        print("Trying char casing")
        for word in self.password.words:
            for i in range(len(word)):
                rebuilt = word[:i] + word[i].upper() + word[i+1:]
                if rebuilt == self.password.original:
                    return True
                
        return False
    
    # apple to 4ppl3, etc
    def try_leet_style(self):
        print("Trying leet style")

        for word in self.password.words:
            for i in word:
                 if i in self.leet_dict:
                      for leet in self.leet_dict[i]:
                            w = word.replace(i, leet)
                            if w == self.password.original:
                                 return True
        return False
    
    def repititon(self):
        print("Trying repitition")
        for word in self.password.words:
              for i in range(1, 4):
                   w = word * i
                   if w == self.password.original:
                    return True
        return False
    
    def dates(self):
        print("Trying dates")

        # Year, desced from curr+1 to 1900
        curr_year = datetime.now().year + 1
        while curr_year > 1900:
            for word in self.password.words:
                if word + str(curr_year) == self.password.original:
                    return True
                if str(curr_year) + word == self.password.original:
                    return True
            curr_year -= 1
        return False