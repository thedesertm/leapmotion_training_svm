import pandas as pd
import os
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pickle

BASE_PATH = os.path.join(os.getcwd() , "dataset")
df = None
i = 0
for file_name in os.listdir(BASE_PATH):
    file_path = os.path.join(BASE_PATH , file_name)
    print(file_path)
    data_frame = pd.read_csv(file_path ,  header=None)
    data_frame.pop(178)
    data_frame.pop(0)
    dat = pd.DataFrame({'result': [i for k in range(data_frame.shape[1])]})
    data_frame = data_frame.join(dat)
    if not df is None :
        df = df.append(data_frame , ignore_index=True)
    else:
        df = data_frame
    i += 1


scaler = StandardScaler()
y = df.pop("result")
scalled_data = scaler.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(scalled_data , y, test_size = 0.20)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
pickle.dump(svclassifier , open("classifier.pkl" , 'wb'))
pickle.dump(scaler , open("scaler.pkl" , 'wb'))