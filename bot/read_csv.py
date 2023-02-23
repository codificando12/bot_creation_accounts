import pandas as pd

def first_name(data):
    df = pd.read_csv(data)
    first_name = [i for i in df['first_name']]
    return first_name
    
def last_name(data):
    df = pd.read_csv(data)
    last_name = [i for i in df['last_name']]

    return last_name

def email(data):
    df = pd.read_csv(data)
    email = [i for i in df['email']]
    return email

def password(data):
    password = [i for i in df['password']] 
    
    return password
    

if __name__ == '__main__':
    read_csv('MOCK_DATA.csv')