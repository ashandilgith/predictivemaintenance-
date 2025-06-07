import pandas as pd 
import numpy as np 


def prepare_data():

    columns = ['unit_number','time_in_cycles', 'setting_1', 'setting_2', 'setting_3'] + [f's_{i}' for i in range(1,2)]

   train_df = pd.read_csv('dir/filename.txt', sep =' ', header=None)

   train_df.drop(columns=[26, 27), in_place = True)

   train_df.columns = columns 

   









