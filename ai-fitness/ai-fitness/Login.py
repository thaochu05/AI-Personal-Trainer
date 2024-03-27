import pickle 
from pathlib import Path

import streamlit_authenticator as stauth 

names =  ["Moc","Thaocute"]
usernames = ['mocmeo','thaocute']
passwords = ['Mocmeo1809', 'Mociuthao0']

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed.pkl"

with open(file_path, "wb") as f:
    pickle.dump(hashed_passwords, f)