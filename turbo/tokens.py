import os, dotenv, datetime, jwt

# Load secrets
dotenv.load_dotenv(override=True)

# Secret key to sign and verify the tokens
SECRET_KEY = os.environ['KEY']

def generate_token(user_id: int, user_name: str, expiration_hours: int = 1):
    current_time = datetime.datetime.utcnow()
    
    payload = {
        'user_id': user_id,
        'user_name': user_name,
        'iat': current_time,
    }

    # Token expiration time
    if expiration_hours != 0:
        expiration_time = current_time + datetime.timedelta(hours=expiration_hours)
        payload['exp'] = expiration_time

    # Generate the token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def validate_token(token, pl=False):
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        
        print('Valid Token')
        return True if not pl else payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        print('Expired Token')
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        print('Invalid token')
        return False
