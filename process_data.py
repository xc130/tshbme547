def read_data():
    in_file = open("test_data.txt", "r")
    return in_file.readlines()


def proc_data(raw_data):
    data = []
    # 'patients' will be a list of dictionaries (one per patient)
    patients = []
    j = 0
    for i in range(len(raw_data)):
        temp = raw_data[i].strip("\n")
        # Stop appending to 'patients' if you've reached the end of the file
        if temp == 'END':
            return data, patients
        data.append(temp)
        # Place new key-value pairs in dictionary
        if i % 4 == 0:
            name = temp.split(' ')
            patients.append({})
            patients[j]['First Name'] = name[0]
            patients[j]['Last Name'] = name[1]
        elif i % 4 == 1:
            patients[j]['Age'] = temp
        elif i % 4 == 2:
            patients[j]['Gender'] = temp
            j += 1
    # return even if file is missing 'END'
    return data, patients


def get_tsh(data):
    tsh_results = []
    tsh_results_str = []
    j = 0
    # convert TSH results into lists of integers for diagnosis and
    # addition to 'patients' dict
    for i in range(len(data)):
        if i % 4 == 3:
            tsh_results_str.append(data[i].split(',')[1:len(data[i])])
            tsh_results.append([float(k) for k in tsh_results_str[-1]])
            j += 1
            # alternatively:
            # tsh_results.append(list(map(float,tsh_results_str)))
    return tsh_results


def diag(input):
    # initially assume normal thyroid function
    ans = 0
    # check for hyper-/hypothyroidism
    for j in range(len(input)):
        if input[j] > 4:
            ans = 1
        elif input[j] < 1:
            ans = -1
    # diagnose accordingly
    if ans == 1:
        diagnosis = "hyperthyroidism"
    elif ans == -1:
        diagnosis = "hypothyroidism"
    else:
        diagnosis = "normal thyroid function"
    return diagnosis


def finish_dict(tsh_results, patients):
    for i in range(len(patients)):
        patients[i]['Diagnosis'] = diag(tsh_results[i])
        patients[i]['TSH results'] = tsh_results[i]
    return patients


def save_result(i):
    import json
    filename = patients[i]['First Name'] + "-"
    filename += patients[i]['Last Name'] + ".json"
    out_file = open(filename, "w")
    json.dump(patients[i], out_file)
    out_file.close()
    return


raw_data = read_data()
# returns cleaned up data and dictionary of patient info
# (except for TSH results and diagnoses)
data, patients = proc_data(raw_data)
tsh_results = get_tsh(data)
# returns dictionary of full patient info
patients = finish_dict(tsh_results, patients)
for i in range(len(patients)):
    save_result(i)
