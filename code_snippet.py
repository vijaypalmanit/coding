from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.metrics import f1_score,recall_score,roc_auc_score,roc_curve,auc


def plot_roc_cur(fper, tper):  
    plt.plot(fper, tper, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()
    
probs = logmodel.predict_proba(x_test)[:,1]    
fper, tper, thresholds = roc_curve(y_test, probs) 
plot_roc_cur(fper, tper)

print(auc(fper, tper))
cf_matrix = confusion_matrix(y_test, predictions)
print(cf_matrix)

import seaborn as sns
sns.heatmap(cf_matrix, annot=True)
labels = ['True Neg','False Pos','False Neg','True Pos']
labels = np.asarray(labels).reshape(2,2)
sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')

from sklearn.ensemble import RandomForestClassifier
# train model
np.random.seed(22)
rfc = RandomForestClassifier(n_estimators=10).fit(x_train, y_train)

from sklearn.utils import resample
X = pd.concat([x_train, y_train], axis=1)

# separate minority and majority classes
not_chargeback = X[X.chargeback==0]
chargeback = X[X.chargeback==1]

# upsample minority
chargeback_upsampled = resample(chargeback,
                          replace=True, # sample with replacement
                          n_samples=len(not_chargeback), # match number in majority class
                          random_state=27) # reproducible results

# combine majority and upsampled minority
upsampled = pd.concat([not_chargeback, chargeback_upsampled])

from imblearn.over_sampling import SMOTE
# setting up testing and training sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

sm = SMOTE(random_state=1, ratio=1.0)
x_train, y_train = sm.fit_sample(x_train, y_train)
