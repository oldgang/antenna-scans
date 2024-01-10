from tabulate import tabulate

def read_data(path):
    filteredData = list()
    with open(path, 'r') as infile:
        for line in infile:
            split = line.split(',')
            filtered = list()
            filtered.append(split[0])
            filtered.append(split[1])
            filtered.append(split[2])
            filtered.append(split[3])
            filteredData.append(filtered)

    #nice printing and sorting
    filteredData.sort(key=lambda row: row[3])
    return tabulate(filteredData, headers=["MAC", "SSID", "Kanał", "Siła sygnału"])

if __name__ == "__main__":
    path = "C:\\Users\\icema\\OneDrive\\Pulpit\\scan.txt"
    filteredData = read_data(path)
    print(filteredData)