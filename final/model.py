# -*- coding: utf-8 -*-
"""
@author: 105502506 106502549
database: https://www.kaggle.com/hugomathien/soccer/data#
Ref: https://www.kaggle.com/c/football-data-challenge
     http://odds.football-data.co.uk/
     https://www.kaggle.com/airback/match-outcome-prediction-in-football
     https://towardsdatascience.com/pandas-for-football-analysis-42c23b252995
"""
import numpy as np 
import pandas as pd 
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

database = 'database.sqlite'
conn = sqlite3.connect(database)
data0 = pd.read_sql("""SELECT Match.id, 
                                        Country.name AS country_name, 
                                        League.name AS league_name, 
                                        season, 
                                        stage, 
                                        date,
                                        HT.team_long_name AS home_team,
                                        HT.team_api_id AS home_id,
                                        AT.team_long_name AS away_team,
                                        AT.team_api_id AS away_id,
                                        home_team_goal, 
                                        away_team_goal                                        
                                FROM Match
                                JOIN Country on Country.id = Match.country_id
                                JOIN League on League.id = Match.league_id
                                LEFT JOIN Team AS HT on HT.team_api_id = Match.home_team_api_id
                                LEFT JOIN Team AS AT on AT.team_api_id = Match.away_team_api_id
                                WHERE country_name in ('Spain', 'Germany', 'France', 'Italy', 'England')
                                
                                ORDER by date
                                LIMIT 100000;""", conn)
data0.head()

data1=data0[["home_team","home_id","away_team","away_id","season","home_team_goal","away_team_goal"]]
data=pd.DataFrame({"HomeTeam":data1.home_team,"HomeID":data1.home_id,"AwayTeam":data1.away_team,"AwayID":data1.away_id,"HTG":data1.home_team_goal,"ATG":data1.away_team_goal})
#print(data1[:5])
#print(data[:40])

# Team goal means
data['HH'] = data['HTG'].groupby(data['HomeTeam']).transform('mean')
data['AH'] = data['HTG'].groupby(data['AwayTeam']).transform('mean')
data['HA'] = data['ATG'].groupby(data['HomeTeam']).transform('mean')
data['AA'] = data['ATG'].groupby(data['AwayTeam']).transform('mean')

data.head()

short2id = pd.read_sql("""SELECT team_api_id AS ID, 
                                 team_Short_name AS short
                                 FROM Team""", conn)

## if Home team is win, win=1
## if Away team is win or draw, win=0
win=[]
for l in range(0,len(data)):
    if data.HTG[l]>data.ATG[l]:
        k1 = 1
        win.append(k1)
    else:
        k1 = 0
        win.append(k1)
df2=pd.DataFrame({"HH":data.HH,"AH":data.AH,"HA":data.HA,"AA":data.AA,"result":win})
df2train, df2test= train_test_split(df2, test_size=0.35, random_state=42)

df2=np.array(df2)
df2test=np.array(df2test)
Y=df2[:,-1]
X=df2[:,:4]
Y1=df2test[:,-1]
X1=df2test[:,:4]

seed = 42

## KNeighbors Model
kfold = model_selection.KFold(n_splits=2, random_state=seed, shuffle=True)
model1 = KNeighborsClassifier()
model1.fit(X,Y.astype('int'))
y_pred = model1.predict(X1)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(Y1, predictions)
print("KNN accuracy: %.2f%%" % (accuracy * 100.0))

## Gaussian Model
kfold = model_selection.KFold(n_splits=2, random_state=seed, shuffle=True)
model2 = GaussianNB()
model2.fit(X,Y.astype('int'))
y_pred = model2.predict(X1)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(Y1, predictions)
print("Gaussian accuracy: %.2f%%" % (accuracy * 100.0))

## Logistic Regression Model
kfold = model_selection.KFold(n_splits=2, random_state=seed, shuffle=True)
model3 = LogisticRegression()
model3.fit(X,Y.astype('int'))
y_pred = model3.predict(X1)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(Y1, predictions)
print("LogReg Accuracy: %.2f%%" % (accuracy * 100.0))


if __name__ == "__main__":
    # KNN
    hhha = [2.81, 0.706]
    ahaa = [1.05, 1.61]
    hhha.insert(1, ahaa[0])
    hhha.append(ahaa[1])
    xx = []
    xx.append(hhha)
    yy1 = model1.predict(xx)
    yy2 = model2.predict(xx)
    yy3 = model3.predict(xx)

    print("\n--Predict result between FC Bayern Munich(H) and Manchester United(A):")
    if yy1 == 1:
        result = 'Win'
    else:
        result = 'Draw/Lose'
    print("-KNN: " + result)
    if yy2 == 1:
        result = 'Win'
    else:
        result = 'Draw/Lose'
    print("-Gaussian: " + result)
    if yy3 == 1:
        result = 'Win'
    else:
        result = 'Draw/Lose'
    print("-LogReg: "+ result)
