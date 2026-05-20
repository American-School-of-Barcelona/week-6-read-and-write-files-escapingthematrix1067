import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    filename = sys.argv[1]
    
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    
    try:
        with open(filename) as f:
            count = 0
            for line in f:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()