import streamlit as st
import pandas as pd
import requests


#title
st.title('Train chatbot')

df=pd.read_csv('D:/Data_Excel/Train chatbot/STATION_CODE.csv')
station=df['Station_code']

#input
A=st.selectbox("Enter the station",station)
B=st.selectbox("Enter the Destination",station)
C=A.split()
D=B.split()
E=st.date_input('Enter the date',format="YYYY-MM-DD")


url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

querystring = {"fromStationCode":C[-1],"toStationCode":D[-1],"dateOfJourney":E}

headers = {
	"X-RapidAPI-Key": "ef5989d22dmsha131e1ecdfacc3ep1b385fjsnbfb018b7aaf8",
	"X-RapidAPI-Host": "irctc1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

Ans=response.json()


a=len(Ans['data'])
for i in range(0,a):
Trno=(Ans['data'][i]['train_number'])
Tname=(Ans['data'][i]['train_name'])
Station=(Ans['data'][i]['from_station_name'])
To=(Ans['data'][i]['to_station_name'])
Class=(Ans['data'][i]['class_type'])
Duration=(Ans['data'][i]['duration'])
Distance=(Ans['data'][i]['distance'])
from_time=(Ans['data'][i]['from_sta'])
to_time=(Ans['data'][i]['to_sta'])





col1, col2,col3 = st.columns(3)


for i in range(0,a):
    with col1:
       st.write(Tname)
       st.markdown(Station)
       st.write(from_time)
       st.write('--------------------------------------------------------------------------------------------------------------------------')
    with col2:
       st.write(Duration)
       st.write('<---------------------------------------->')
       st.write(Distance)
       st.write('--------------------------------------------------------------------------------------------------------------------------')
    with col3:
       st.write(Trno)
       st.markdown(To)
       st.write(to_time)
       st.write('--------------------------------------------------------------------------------------------------------------------------')