def read_data():
    in_file = open("test_data.txt","r")
    return in_file.readlines()

def proc_data(raw_data):
    data = []
    patients = []
    j = 0
    for i in range(len(raw_data)):
        temp = raw_data[i].strip("\n")
        if temp == 'END':
            return data, patients
        data.append(temp)
        if i % 4 == 0:
            name = temp.split(' ')
            patients.append({})
            patients[j]['First name'] = name[0]
            patients[j]['Last name'] = name[1]
            print(patients[j])
        elif i % 4 == 1:
            patients[j]['Age'] = temp
        elif i % 4 == 2:
            patients[j]['Gender'] = temp
            j += 1

def diag(data,patients):
    tsh_results = []
    tsh_results_str = []
    diagnoses = []
    j = 0
    # convert TSH results into lists of integers
    for i in range(len(data)):
        if i % 4 == 3:
            tsh_results_str.append(data[i].split(',')[1:len(data[i])])
            tsh_results.append([float(k) for k in tsh_results_str[-1]])
            patients[j]['TSH results'] = tsh_results[-1]
            j += 1
            # alternatively:
            # tsh_results.append(list(map(float,tsh_results_str)))
    # check range of TSH results
    for i in range(len(tsh_results)):
        temp = tsh_results[i]
        # initially assume normal thyroid function
        ans = 0
        # check for hyper-/hypothyroidism
        for j in range(len(temp)):
            if temp[j] > 4:
                ans = 1
            elif temp[j] < 1:
                ans = -1
        # diagnose accordingly
        if ans == 1:
            diagnoses.append("hyperthyroidism")
        elif ans == -1:
            diagnoses.append("hypothyroidism")
        else:
            diagnoses.append("normal thyroid function")
        patients[i]['diagnosis'] = diagnoses[-1]
    print(patients)
    return patients

def save_result(i):
    import json
    filename = patients[i]['First name'] + "-" + patients[i]['Last name'] + ".json"
    out_file = open(filename,"w")
    json.dump(patients[i],out_file)
    out_file.close()
    return

raw_data = read_data()
# returns cleaned up data and dictionary of patient info (except for TSH results and diagnoses)
data, patients = proc_data(raw_data)
# returns dictionary of full patient info
patients = diag(data,patients)
for i in range(len(patients)):
    save_result(i)
