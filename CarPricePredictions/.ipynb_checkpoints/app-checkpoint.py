import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('randomForestRegressionModel.pkl','rb'))

def predict():
  Year = int(st.number_input("Enter the Year of Purchase:"))
  Present_Price = float(st.number_input("Enter the Present price of the car:"))
  Kms_Driven = int(st.number_input("Enter the Kilometers Driven:"))
  # if Kms_Driven == 0:
  #   Kms_Driven = 1
  # Kms_Driven2 = np.log(Kms_Driven)
  Owner = int(st.number_input("Enter the number of Owners:"))

  Fuel_Type_Petrol = st.selectbox("Select Fuel Type",['Petrol','Diesel'])
  if Fuel_Type_Petrol == 'Petrol':
    Fuel_Type_Petrol = 1
    Fuel_Type_Diesel = 0
  else:
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 1

  Year = 2023 - Year

  Seller_Type_Individual = st.selectbox('Select the Seller Type',['Individual','Dealer'])
  if Seller_Type_Individual == 'Individual':
    Seller_Type_Individual = 1
  else:
    Seller_Type_Individual = 0

  Transmission_Manual = st.selectbox('Select Transmission',['Manual','Automatic'])
  if Transmission_Manual == 'Manual':
    Transmission_Manual = 1
  else:
    Transmission_Manual = 0

  prediction = model.predict([[Present_Price,Kms_Driven, Owner, Year, Fuel_Type_Diesel,Fuel_Type_Petrol, Seller_Type_Individual,Transmission_Manual]])

  output = round(prediction[0],2)

  if output<0:
    st.error("Sorry you cannot sell this car")
  else:
    st.success("You can sell the car at {}".format(output))



def main():
  st.title("Car Price Prediction")
  st.subheader("Built by Suyog Dhakal")
  predict()

if __name__ == '__main__':
  main()