import os
import pickle


#Load Model
def futureweeksprediction(n, ci):

    ci = (100-ci)*0.01

    with open('model_superstore_sales.pkl', 'rb') as file:
        print('Model Loaded')
        model = pickle.load(file)
        print(model)

    forecast = model.forecast(steps=n) # making a forecast of n weeks later of the last date in the 'Date' column

    forecast2 = model.get_forecast(steps=n)
    df_forecast2 = forecast2.summary_frame(alpha=ci)

    dates = forecast.index
    sales = forecast.values
    mean_ci_lower = list(df_forecast2.mean_ci_lower.values)
    mean_ci_upper = list(df_forecast2.mean_ci_upper.values)

    #print(dates, sales, mean_ci_lower, mean_ci_upper)

    futureweekslist = []

    for i in range(len(sales)):
        val1 = str(dates[i])
        val2 = sales[i]
        val3 = mean_ci_lower[i]
        val4 = mean_ci_upper[i]
        futureweekslist.append({'Date': val1,
                                'Sales': val2,
                                'Mean_CI_lower': val3,
                                'Mean_CI_upper': val4})

    #print('futureweekslist: ', futureweekslist)

    return futureweekslist