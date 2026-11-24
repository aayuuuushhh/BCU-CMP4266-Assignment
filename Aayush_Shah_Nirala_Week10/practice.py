with open("city.txt", "r") as fin:

    header = fin.readline()

    maxpop = 0
    maxcity = ""
    found = False

    # Read each line
    for line in fin:
        fields = line.strip().split(";")  # split by semicolon

        if len(fields) == 3:  # City;Country;Population
            city = fields[0].strip()
            country = fields[1].strip()
            try:
                population = int(fields[2].strip())
            except ValueError:
                population = 0

            if country == "UK":
                found = True
                if population > maxpop:
                    maxpop = population
                    maxcity = city

# Final output
if not found:
    print("No UK cities in input file.\n")
else:
    print(f"Largest city in UK is {maxcity} with population {maxpop}.")