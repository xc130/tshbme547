from process_data import diag
import pytest


@pytest.mark.parametrize("inputs, exp",
                         [([3.0, 4.0, 1.0], "normal thyroid function"),
                          ([2.0, 3.2, 4.1, 3.9], "hyperthyroidism"),
                          ([0.9, 0.8, 3.6], "hypothyroidism")])
def test_correct_diag(inputs, exp):
    """Tests diagnosis function

    Tests the 'diag' function in process_data.py, checking if the actual
    output corresponds to the expected output

    Args:
        inputs (list): made up TSH results for one patient
        exp (string): expected diagnosis for that input

    Returns:
        none
    """

    ans = diag(inputs)
    print(ans)
    assert ans == exp
