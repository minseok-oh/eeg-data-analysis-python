import sys, os
import numpy as np
import pandas as pd
from scipy.fft import fft, ifft
sys.path.append(os.path.abspath('../'))

import utils
DATA_FOLDER = '<dataset>'
CWT_NUMBER = '<t0>'

def psi(T, f0=6):
    x = np.linspace(-2*np.pi, 2*np.pi, T)
    return (np.pi**-0.25) * np.exp(1j*f0*x - x**2/2)

def wavelet_convolution(tup):
    f=tup[0]
    T=tup[1]
    f_len=np.shape(f)[0]
    f_hat=np.append(f,np.zeros(T))
    h=psi(T)
    h_hat=np.append(h,np.zeros(f_len))

    return ifft(fft(f_hat)*fft(h_hat))[round(T/2):round(T/2)+f_len]

def cwt(f, t0):
    f_len = np.shape(f)[0]
    result = wavelet_convolution([f, t0])
    return result

if __name__ == '__main__':
    # 원하는 data의 경로와 형식을 적으세요
    subject_filenames = utils.find_csv_filenames("<dataset>", "<suffix>") 

    for name in subject_filenames:
        df = pd.read_csv(name)

        merged_df = {}
        for i in range(df.shape[1]):
            here = pd.Series(cwt(df.iloc[:, i].to_numpy(), 10))
            merged_df[i] = here
        merged_df = pd.DataFrame(merged_df)

        # 저장이 되길 원하는 경로와 형식을 적으세요
        merged_df.to_csv("<output>".format("<suffix>"), index=False)