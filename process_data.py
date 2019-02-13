def read_data():
    in_file = open("test_data.txt","r")
    return in_file.readlines()

def save_result():
    import json
    out_file = open("results.json","w")
    json.dump(results,out_file)
    out_file.close()
    return

raw_data = read_data()
data = []
tsh_results = []

for i in range(len(raw_data)):
    data.append(raw_data[i].strip("\n"))

for i in range(len(data)):
    if i % 4 == 3:
        tsh_results.append(data[i].split(',')[1:len(data[i])])

print(tsh_results)
