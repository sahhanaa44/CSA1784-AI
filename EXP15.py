from sklearn.tree import DecisionTreeClassifier

X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

y = [0,0,1,1]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[1,0]])

print("Prediction =", prediction[0])
