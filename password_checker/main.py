import sys
import time
from classes.password import Password

def main():
    ts_start = time.time()
    print(ts_start)
    use_password = None
    if len(sys.argv) == 2:
        use_password = sys.argv[1]
    else:
        use_password = 'sieni'
    pw = Password(use_password.strip())

    if pw.is_in_lists():
        print(f"The password \"{pw.original}\" was found in common word lists")
    else:
        print(f"The password \"{pw.original}\" was not found in common word lists, extending to rulesets")
        if pw.apply_ruleset():
            print(f"The password \"{pw.original}\" was found on ruleset apply")

    print(f"Finished main application in {time.time() - ts_start} seconds")

if __name__ == "__main__":
    main() 