GitHub repo for xc130 hw 3 (TSH test data conversion assignment)

Contains 2 Python files (process_data.py and test_process_data.py). process_data.py reads in patient data from test_data.txt, diagnoses each patient based on their TSH results, and then outputs the relevant patient dictionary to a .JSON file for each patient (with the title 'FirstName-LastName.json'). test_process_data.py tests the previous file to check that the function that diagnoses patients works as expected.

A new file, 'one_pat.txt' was also added to check that process_data.py works even if only one patient's data is read in.

This repository also contains requirements.txt and .travis.yml files to allow use of pytest and Travis-CI.

Two patients' .JSON files have also been uploaded.

# tshbme547
