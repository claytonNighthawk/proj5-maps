"""
Test program for processing location data
"""

def process(raw): 
    locations = [] 
    file = open(raw)
    for line in file:
        line = line.strip()
        print(line)
        if len(line) == 0 or line[0] == '#':
            continue
        parts = line.split(',')
        locations.append({"lat": float(parts[0]), "lng": float(parts[1])})

    file.close()
    return locations

def main():
    f = "./data/locations.txt"
    parsed = process(f)
    print(parsed)

if __name__ == "__main__":
    main()