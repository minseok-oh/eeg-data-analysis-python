import sys, os
from os import listdir
import pandas as pd

sys.path.append(os.path.abspath('../'))
import utils

# 제거를 원하는 column을 적으세요
UNWANTED_COLS = []

# csv 파일을 합쳐주는 함수입니다
def merge_csv_file(csv_list):
    merged_df = pd.DataFrame()
    for subject_name in csv_list:
        df = pd.read_csv(subject_name)
        merged_df = merged_df.append(df, ignore_index=True)
    return merged_df
    
if __name__ == '__main__':
    # 원하는 data의 경로와 형식을 적으세요
    subject_filenames = utils.find_csv_filenames("<dataset>", "<suffix>") 

    for name in subject_filenames:
        df = pd.read_csv(name)
        df.drop(UNWANTED_COLS, axis=1, inplace=True)

        # 저장이 되길 원하는 경로와 형식을 적으세요
        df.to_csv("<output>".format("<suffix>"), index=False)