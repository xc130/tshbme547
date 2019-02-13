def read_data():
    """Read data from file

    This function reads in data from a text file containing patient information

    Args:
        none

    Returns:
        in_file.readlines() (list): the test data text file, parsed in line by
        line
    """
    in_file = open("test_data.txt", "r")
    return in_file.readlines()


def proc_data(raw_data):
    """Processes data

    This function cleans up the raw input from the data file, stripping all
    "\n", and then fills the name, age and gender key-value pairs for each
    patient's dictionary. It then returns the cleaned data and the list of
    patient dictionaries

    Args:
        raw_data (list): data as parsed in from the test data text file

    Returns:
        data (list): list of all patient data with "\n" removed
        patients (list): list containing dictionaries with partial patient info
    """
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
    """Gets TSH results in float format

    The TSH results from the test file, when read in, appear as one string
    per patient. This function takes the string and splits it up by comma.
    It then converts those strings into floats and places those floats back
    into a list (one per patient).

    Args:
        data (list): patient data (all)

    Returns:
        tsh_results (list): list of lists of patient TSH results

    """
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
    """Patient diagnosis from TSH results

    This function takes a list of TSH results for one patient and checks if
    any result is above 4.0 (in which case it diagnoses "hyperthyroidism"),
    below 1.0 (in which case it diagnoses "hypothyroidism"), or between 1.0
    and 4.0, inclusive (diagnoses "normal thyroid function").

    Args:
        input (list): list of TSH results

    Returns:
        diagnosis (string): string containing diagnosis based on TSH results
        (one of the three options above)
    """
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
    """Finishes up each patient's dictionary

    So far, all the key-value pairs for each patient's dictionary except for
    'Diagnosis' and 'TSH' have been filled. This function completes the job.

    Args:
        tsh_results (list): list of lists of patient TSH results
        patients (list): partially filled list of patient dictionaries

    Returns:
        patients (list): complete list of patient dictionaries
    """
    for i in range(len(patients)):
        patients[i]['Diagnosis'] = diag(tsh_results[i])
        tsh_results[i].sort()
        patients[i]['TSH'] = tsh_results[i]
    return patients


def save_result(i):
    """Saves patient dictionary to JSON file

    Will be called once for each patient in text file. This function saves
    each patient's dictionary to an accordingly named JSON file
    (FirstName-LastName.json)

    Args:
        i (int): patient index in text file

    Returns:
        none
    """
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
