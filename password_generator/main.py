import sys
from password import Password

def main():
    use_password = None
    if len(sys.argv) == 2:
        use_password = sys.argv[1]
    else:
        use_password = 'sieni'
    pw = Password(use_password.strip())

    if pw.is_in_lists():
        print(f"The password was found in common word lists")
    else:
        print(f"The password was not found in common word lists, extending to rulesets")
        pw.read_rulesets()

    print(f"Finished main application")

if __name__ == "__main__":
    main() 