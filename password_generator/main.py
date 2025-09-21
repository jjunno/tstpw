import sys
from password import Password

def main():
    use_password = None
    if len(sys.argv) is 2:
        use_password = sys.argv[1]
    else:
        use_password = 'sieni'
    pw = Password(use_password)
    pw.generate()

if __name__ == "__main__":
    main() 