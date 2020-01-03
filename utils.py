import numpy as np

def ascii_list_to_ndarray(ascii_list):
    return None

def extract_effi_ct(transfer_matrix):
    efficiency = []
    crosstalk = []
    for row in transfer_matrix:
        for col in row:
            if row == col:
                efficiency.append(transfer_matrix[row, col])
            else:
                crosstalk.append(transfer_matrix[row, col])

    max_effi = np.max(efficiency)
    ave_effi = np.average(efficiency)
    max_ct = np.max(crosstalk)
    ave_ct = np.average(crosstalk)

    return max_effi, ave_effi, max_ct, ave_ct

def extract_ave_effi(transfer_matrix):
    nrow, ncol = transfer_matrix.shape
    efficiency = np.array([transfer_matrix[i,i] for i in range(nrow)])
    return np.average(efficiency)
