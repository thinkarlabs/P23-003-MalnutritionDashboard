import time
import jwt
from configparser import ConfigParser

config = ConfigParser()
config.read(".config")
config = config["JWT"]

JWT_SECRET = config["secret"]
JWT_ALGORITHM = config["algorithm"]

def token_resp(token:str):
    return {"access token":token}
    
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time()+600
    }
    print(JWT_SECRET)
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_resp(token)
    
def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except Exception as e:
        print("Issue In decodeJWT", e)
        return None
