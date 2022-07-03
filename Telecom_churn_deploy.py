import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import pickle
from flask import Flask, request, render_template

from flask import Flask
app = Flask(__name__)


@app.route("/")
def loadPage():
    return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def Tele_ChurnPrediction():

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']

    model = pickle.load(open("Telemodel.sav", "rb"))

    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7,
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19]]

    new_df = pd.DataFrame(data, columns=['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender',
                                         'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
                                         'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                         'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                         'PaymentMethod', 'tenure'])

    #final_df=pd.concat([new_df__dummies, new_dummy], axis=1)

    single = model.predict(new_df)
    probablity = model.predict_proba(new_df)[:, 1]

    if single == 1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)

    return render_template('home.html', output1=o1, output2=o2,
                           query1=request.form['query1'],
                           query2=request.form['query2'],
                           query3=request.form['query3'],
                           query4=request.form['query4'],
                           query5=request.form['query5'],
                           query6=request.form['query6'],
                           query7=request.form['query7'],
                           query8=request.form['query8'],
                           query9=request.form['query9'],
                           query10=request.form['query10'],
                           query11=request.form['query11'],
                           query12=request.form['query12'],
                           query13=request.form['query13'],
                           query14=request.form['query14'],
                           query15=request.form['query15'],
                           query16=request.form['query16'],
                           query17=request.form['query17'],
                           query18=request.form['query18'],
                           query19=request.form['query19'])


app.run(debug=True)
