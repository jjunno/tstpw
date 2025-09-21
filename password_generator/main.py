from password import Password

def main():
    testInput = 'korhonen'
    pw = Password(testInput)
    pw.read_files()

if __name__ == "__main__":
    main() 