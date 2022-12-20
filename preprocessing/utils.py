import os
import pandas as pd

def integral(x: list, y: list, start: int, end: int) -> int:
    mask = (start < x < end)
    y_range = y[mask]
    return y_range.sum() / y_range.shape[0]


def decomp_wave(x: list, y: list) -> dict:
    WAVE_CONST = [ 0.2, 4.0, 8.0, 13.0, 30.0, 50.0 ]
    ignore_const = 0.01
    return {
        'delta': integral(x, y, WAVE_CONST[0], WAVE_CONST[1] - ignore_const),
        'theta': integral(x, y, WAVE_CONST[1], WAVE_CONST[2] - ignore_const),
        'alpha': integral(x, y, WAVE_CONST[2], WAVE_CONST[3] - ignore_const),
        'beta': integral(x, y, WAVE_CONST[3], WAVE_CONST[4] - ignore_const),
        'gamma': integral(x, y, WAVE_CONST[4], WAVE_CONST[5] - ignore_const),
    }

def load_data(filename):
    df = pd.read_csv(filename)
    return df

def find_csv_filenames(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [os.path.join(path_to_dir, filename) for filename in filenames if filename.endswith(suffix)]