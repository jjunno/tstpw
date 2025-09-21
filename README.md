# tstpw
No-depedency, quick password iterator/test/check.

Take user input, iterate it through material, custom ruleset and predefined rudimentary custom logic.
Command line feedback returns true if password was "found" or not.

If the password was "found", it means that it was either found from common wordlists/passwordlists or by using simple logic to prepend/append extra charaters.

## Why
I simply wanted to spend the rainy sunday morning doing this. It's common to use something like your firstname as your password. To make it hackproof, folk is known add 1 or ! or current year. I just wanted to see how long does it take to build a simple tool to check if password is useless. It didn't take long.

# Usage
```
git clone https://github.com/jjunno/tstpw.git

python3 password_checker/main.py {password}
python3 password_checker/main.py trustno1
python3 password_checker/main.py trustno1!
```

## Custom ruleset
A custom ruleset can be applied, see material/rulesets/common.txt. Either by appending rules or creating a new .txt file in /material/rulesets.
A single line is a single rule. The rule will be prepended and appended.

If you test password "foobar69" and you have "69" in your ruleset, the application will check if foobar69 or 69foobar matches.

### Predefined logic
The application contains rudimentary logic for following rules. You do not need to apply these in custom rulesets.
```
```
* The whole password will be uppercased
    * From apple to APPLE
* Characters will be iterated and uppercased
    *  Apple, aPple, apPle ...
* Leet style character replacing
    * From apple to 4ppl3 and @ppl3 ...
* Password will be repeated until three times
    * apple, appleapple ...
* Decrement date iteration from current year + 1 until 1900. Both prepend and append
    * apple2025, 2024apple, 2000apple, apple2018

# Parsers
Parses are there in case the material is updated (manually).

# To do
What to do maybe next rainy sunday.

* Improve dates to use YYYYmmdd instead of year only
* List of alphabets and combinations to prepend and append

# Material sources
## Lang FI
```
https://kotus.fi/sanakirjat/kielitoimiston-sanakirja/nykysuomen-sana-aineistot/nykysuomen-sanalista/
```

## Firstnames both men and women FI
```
https://www.avoindata.fi/data/fi/dataset/none
```


## Surnames FI
```
https://www.avoindata.fi/data/fi/dataset/none
```

## Common credentials
```
https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
```