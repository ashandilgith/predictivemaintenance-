import pandas as pd 
import numpy as np 


def prepare_data():

    #load the data as a pandas dataset 

    train_df = pd.read_csv('dir/filename.txt', sep = ' ', header=None)

    #name the columns 
    columns = ['unit_number', 'time_in_cycles', 'setting_1', 'setting_2', 'setting'] + [f's_{i}' for i in range (1,22)]

    #name the columns of the new dataset
    train_df.columns = columns 

    #calculate Remaining Useful Life for each machine (unit_number on the table), by:
    # 1. changing max cycle series to just the highest number (as it's currently a series of numbered runs)
    # 2. simply changing max cycle to RUL by just removing the number of cycles run so far

   # Calculate RUL for the training data

    # 1️⃣ Group by unit_number (machine ID) and get the final cycle (maximum time_in_cycles) for each unit
    max_cycles = train_df.groupby('unit_number')['time_in_cycles'].max()
    #max_cycles = train_df.groupby('unit_number')['time_in_cycles'].max()
    #max_cycles = train_df/groupby('unit_number')['time_in_cycles'].max()
    #max_cycles = train_df.groupby('unit_number')['time_in_cycles'].max()

    # 2️⃣ Merge the max_cycles back into the original dataframe, adding a 'max_cycle' column for each record based on unit_number
    train_df = train_df.merge(max_cycles.to_frame(name='max_cycle'), left_on='unit_number', right_index=True)
    #train_df = train_df.merge(max_cycles.to_frame(name='max_cycle'), left_on = 'unit_number', right_index=True)

    # 3️⃣ Calculate RUL by subtracting current cycle from the final cycle for each record
    train_df['RUL'] = train_df['max_cycle'] - train_df['time_in_cycles']
    #train_df['RUL'] = train_df['max_cycle'] - train_df['time_in_cycles']

    # 4️⃣ Drop the now-unnecessary 'max_cycle' column since we've already computed RUL
    train_df.drop(columns=['max_cycle'], inplace=True)

    #save the processed data 
    train_ds.to_csv('dir/filename.csv', index=False)


if __name__ == "__main__": 
    prepare_data()






   









