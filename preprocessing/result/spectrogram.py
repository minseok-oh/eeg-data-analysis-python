import sys, os
import numpy as np
import pandas as pd
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath('../'))

import utils

DATA_FOLDER = '<dataset>'
NFFT_DATA = [ 4096, 32768 ]
FS_DATA = [ 8192, 32768, 65536 ]

if __name__ == '__main__':
    # 원하는 data의 경로와 형식을 적으세요
    subject_filenames = utils.find_csv_filenames("<dataset>", "<suffix>") 

    for name in subject_filenames:
        df = utils.load_data(name)

        # 축과 공백이 없는 사진을 만들기 위해서 sybplots_adjust와 axis를 사용하였습니다
        fig = plt.figure(figsize=(12, 10))
        fig.subplots_adjust(hspace=0, wspace=0)

        for i in range(df.shape[1]-1):
            ax = fig.add_subplot(6, 3, i+1)
            ax.specgram(df.iloc[:, i], NFFT='<input nfft>', Fs='<input fs>', noverlap=int('<input nfft>' / '<input overlap>'))
            ax.axis('off')
        # 마지막으로 <name>.png의 형태로 파일이 저장됩니다
        plt.savefig(f'<{name}>.png')