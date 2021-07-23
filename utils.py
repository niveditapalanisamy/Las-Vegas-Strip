import numpy as np 
import joblib 


def preprocessdata(Period_of_stay,Traveler_type,Pool,Gym,Tennis_court,Spa,Casino,Free_internet,Hotel_stars,Member_years,Review_month,Review_weekday):
    test_data = [[Period_of_stay,Traveler_type,Pool,Gym,Tennis_court,Spa,Casino,Free_internet,Hotel_stars,Member_years,Review_month,Review_weekday] ]
    trained_model = joblib.load("model.pkl") 

    prediction = trained_model.predict(test_data) 

    return prediction 
