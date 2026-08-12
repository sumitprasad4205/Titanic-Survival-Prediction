from flask import Flask,render_template,request
import pandas as pd
import joblib

app = Flask(__name__)

m = joblib.load('titanic.pkl')
model = m['LogisticRegression']

def feature_engineering(df):
    df['SibSp'] = pd.to_numeric(df['SibSp'])
    df['Parch'] = pd.to_numeric(df['Parch'])
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['Title'] = df['Name'].str.extract(r', (.*?)\.')
    df['TicketSize'] = df['Ticket'].value_counts()
    df['HasCabin'] = df['Cabin'].notnull().astype(int)

    df.drop(['SibSp','Parch','Ticket','Cabin'],axis=1,inplace=True)
    return df

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method== 'POST':
        Pclass = request.form['Pclass']
        Name = request.form['Name']
        Sex = request.form['Sex']
        Age = request.form['Age']
        SibSp = request.form['SibSp']
        Parch = request.form['Parch']
        Ticket = request.form['Ticket']
        Fare = float(request.form['Fare'])
        Cabin = request.form['Cabin']
        Embarked = request.form['Embarked']

        data = {
            'Pclass':Pclass,
            'Name':Name,
            'Sex':Sex,
            'Age':Age,
            'SibSp':SibSp,
            'Parch':Parch,
            'Ticket':Ticket,
            'Fare': Fare,
            'Cabin':Cabin,
            'Embarked':Embarked
        }
        feature = pd.DataFrame([data])
        features = feature_engineering(feature)

        prediction = model.predict(features)
        if prediction[0]==1:
            predicted_text= "Passenger Survived"
        else:
            predicted_text= "Passenger Not Survived"
        return render_template('index.html',predicted_text= f'{predicted_text}')

    return render_template('index.html')

app.run(debug=True)
