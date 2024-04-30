import pyrebase
import getpass

firebaseConfig = {
  "apiKey": "AIzaSyDi0cwvT-FOz5xwlvYwGmFGeUEKeUGjrBM",
  "authDomain": "infosec-firebase.firebaseapp.com",
  "projectId": "infosec-firebase",
  "storageBucket": "infosec-firebase.appspot.com",
  "messagingSenderId": "103612261109",
  "appId": "1:103612261109:web:7a30e0118ef99479555bbc",
  "measurementId": "G-EBLCGERSQM",
  "databaseURL": "https://infosec-firebase.firebase.io"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = input("[+]Write your email here\n")
passwd = getpass.getpass("[+]Digite sua senha com pelo menos 6 caracteress")
status = auth.sign_in_with_email_and_password(user, passwd)

idToken  = status["idToken"]
info = auth.get_account_info(idToken)

print(idToken)

