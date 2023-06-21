from tabulate import tabulate
scan_data = list()
filtered_data = list()
with open("C:\\Users\\icema\\OneDrive\\Pulpit\\scan.txt", 'r') as infile:
    for line in infile:
        split = line.split(',')
        filtered = list()
        filtered.append(split[0])
        filtered.append(split[1])
        filtered.append(split[2])
        filtered.append(split[3])
        filtered_data.append(filtered)

#nice printing and sorting
filtered_data.sort(key=lambda row: row[3])
print (tabulate(filtered_data, headers=["MAC", "SSID", "Channel", "Signal Strength"]))
