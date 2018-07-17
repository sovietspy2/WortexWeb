import hashlib
import WortexLogger


def get_hashed_pasword(plain_text):
    hash_object = hashlib.sha256(str(plain_text).encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def check_hashed_passwords(plain_text, value_from_db):
    #WortexLogger.logging.info(f"HASHED {get_hashed_pasword(str(plain_text).encode())} and FROMDB: {value_from_db}")
    return get_hashed_pasword(str(plain_text))==value_from_db