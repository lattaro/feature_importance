model  = RandomForestClassifier() #Escolha do modelo
model.fit(X_train, y_train) #treinamento
model.feature_importances_
importances = pd.Series(data=model.feature_importances_,index=X_train.columns)
sns.barplot(x=importances, y=importances.index, orient='h').set_title('Importância de cada feature') #visualização gráfica
