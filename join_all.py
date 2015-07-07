import pandas as pd

label_train = pd.read_csv('../data/train/truth_train.csv', header=False,nrows=1000)

enroll = pd.read_csv('feature/enrollment_feature.csv', header=False)
log = pd.read_csv('feature/log_feature.csv', header=False, nrows=1000)
obj = pd.read_csv('feature/obj_feature.csv', header=False)

merged = pd.merge(enroll, log, on='enrollment_id', how='inner')
pd.merge(merged, obj, on='enrollment_id', how='inner').to_csv('feature/all_total.csv')
