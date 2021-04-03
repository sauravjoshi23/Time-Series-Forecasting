import os
import pickle
import pandas as pd

#Load Model
def pastweeksprediction(n, ci):

    ci = (100-ci)*0.01

    with open('model_superstore_sales.pkl', 'rb') as file:
        print('Model Loaded')
        model = pickle.load(file)
        print(model)

    # print('Model Loaded Past')
    # model = pd.read_pickle('model_superstore_sales.pkl')

    data = pd.read_csv('Weekly_data.csv', index_col=0, parse_dates=True)

    print(data.head())

    pred = model.get_prediction(start=pd.to_datetime('2015-01-04'), dynamic = False)  # making a prediction of n weeks in recent past of the latest date in the 'Date' column
    true_values = data["2015-01-04":]

    pred2 = pred.summary_frame(alpha=ci)

    dates = data.index[-n:]
    sales = list(pred2['mean'].values)[-n:]
    true_values = data['Sales'][-n:]
    mean_ci_lower = list(pred2.mean_ci_lower.values)[-n:]
    mean_ci_upper = list(pred2.mean_ci_upper.values)[-n:]

    #print(dates, sales, mean_ci_lower, mean_ci_upper)

    pastweekslist = []

    for i in range(len(sales)):
        val1 = str(dates[i])
        val2 = sales[i]
        val3 = mean_ci_lower[i]
        val4 = mean_ci_upper[i]
        val5 = true_values[i]
        pastweekslist.append({'Date': val1,
                                'Sales': val2,
                                'Mean_CI_lower': val3,
                                'Mean_CI_upper': val4,
                                'True_Sales': val5})

    print('Pastweekslist: ', pastweekslist)

    return pastweekslist