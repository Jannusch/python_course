import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from an api and return a parsed json object
def get_data(link: str) -> dict:
    response = requests.get(link)
    values = json.loads(response.text)
    return values



# Create a pandas dataframe from a json object
def create_dataframe(json_data: dict, name: str) -> pd.DataFrame:
    df = pd.DataFrame(json_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # use timestamp as index
    df = df.set_index('timestamp')
    # change name of value column
    df = df.rename(columns={'value': name})
    return df

def create_line_plot(df):
    plt.figure(figsize=(10,6))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Line Plot')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    link = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/7cb7461b-3530-4c01-8978-7f676b8f71ed/W/measurements.json?start=P100D"
    link_2 = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/70272185-b2b3-4178-96b8-43bea330dcae/W/measurements.json?start=P100D"
    data = get_data(link)
    data = create_dataframe(data, "Schöne")
    data_2 = get_data(link_2)
    data_2 = create_dataframe(data_2, "Dresden")

    # merge data frames
    data = pd.merge(data, data_2, on='timestamp')
    
    print(data.head())
    create_line_plot(data)
    plt_2 = data.plot()
    plt_2.figure.savefig("plot.png")
