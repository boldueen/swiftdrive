import os
import openpyxl
import csv
import shutil
import pandas as pd
from tempfile import NamedTemporaryFile
from openpyxl import load_workbook
from openpyxl.workbook import Workbook


def get_info_from_csv_by_manager_id(id:int, csv_path:str) -> dict:
    id = str(id)
    with open(csv_path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            if row['manager_id'] == id:
                return row


def get_all_info_from_csv(csv_path:str) -> list:
    all_data = list()
    with open(csv_path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            all_data.append(row)

    return(all_data) 


def get_target_rides_info_by_manager_name_from_csv(csv_path:str, manager_name:str):
        df = pd.read_csv(csv_path)
        ds = df[df['full_name']==manager_name]
        return int(ds['target_rides'][0])
        

def get_ratio_info_by_manager_name_from_csv(csv_path:str, manager_name:str):
        df = pd.read_csv(csv_path)
        rides_as_unit_of_ratio = df[df['full_name']==manager_name][rides_as_unit_of_ratio][0]
        return rides_as_unit_of_ratio


def get_manager_id_by_name_from_csv(csv_path:str, manager_name:str) -> int:
    df = pd.read_csv(csv_path)
    ds = df[df['full_name'] == manager_name]
    return int(ds['manager_id'][0])


def get_target_gp_by_name_from_csv(csv_path:str, manager_name:str) -> int:
    df = pd.read_csv(csv_path)
    ds = df[df['full_name'] == manager_name]
    return int(ds['target_gp'][0])




def set_info_to_csv_by_manager_name(csv_path:str, manager_name:str, rides_as_unit_of_ratio=0, targer_rides=0):
    id = get_manager_id_by_name_from_csv(csv_path, manager_name)
    
    old_data = pd.read_csv(csv_path)
    
    targer_rides_to_write = old_data.iloc[id]['target_rides']
    rides_as_unit_of_ratio_to_write = old_data.iloc[id]['rides_as_unit_of_ratio']

    if targer_rides != 0:
        targer_rides_to_write=targer_rides
    
    if rides_as_unit_of_ratio != 0:
        rides_as_unit_of_ratio_to_write = rides_as_unit_of_ratio


    df = pd.read_csv('data_example.csv')
    df.loc[id, 'target_rides'] = targer_rides_to_write
    df.loc[id, 'rides_as_unit_of_ratio'] = rides_as_unit_of_ratio_to_write
    df.to_csv('data_example.csv', index=False)

    print('data for ' + manager_name + ' successfully changed')


def set_info_to_csv_by_manager_id(csv_path:str, id:int, rides_as_unit_of_ratio=0, targer_rides=0):
    old_data = pd.read_csv(csv_path)
    
    targer_rides_to_write = old_data.iloc[id]['target_rides']
    rides_as_unit_of_ratio_to_write = old_data.iloc[id]['rides_as_unit_of_ratio']

    if targer_rides != 0:
        targer_rides_to_write=targer_rides
    
    if rides_as_unit_of_ratio != 0:
        rides_as_unit_of_ratio_to_write = rides_as_unit_of_ratio


    df = pd.read_csv('data_example.csv')
    df.loc[id, 'target_rides'] = targer_rides_to_write
    df.loc[id, 'rides_as_unit_of_ratio'] = rides_as_unit_of_ratio_to_write
    df.to_csv('data_example.csv', index=False)



def create_daily_report_from_file(filepath:str='reports/daily_report.xlsx', data_filepath:str='downloads/CustomersReports.xlsx', csv_path:str='data_example.csv'):

    manager_name = 'Бутова Светлана'
    df = pd.read_excel(data_filepath, 'sheet1')
    ds = df[df['Менеджер'] == manager_name].sum(numeric_only=True)
    print(ds[[2,4,5,7,8,9]])


    fact_rides = ds[2]
    GMV = ds[4]
    target_rides = get_target_rides_info_by_manager_name_from_csv(csv_path, manager_name)
    fact_vs_target = round((fact_rides/target_rides)*100,2)

    customers_with_access_to_personal_account = ds[7]
    FTR_users = ds[8]
    STR_users = ds[9]
    total_active_users = FTR_users + STR_users

    margin_GP = ds[5]
    GP_per_ride = round(margin_GP/fact_rides,2)
    GP_client_check = margin_GP/GMV

    target_gp = get_target_gp_by_name_from_csv(csv_path, manager_name)
