import os, dotenv, datetime, jwt

# Load secrets
dotenv.load_dotenv(override=True)

# Secret key to sign and verify the tokens
SECRET_KEY = os.environ['SECRET_KEY']

def generate_token(user_id: int, user_name: str, expiration_hours: int = 1):
    """
    Generates a token for the given user ID and user name with an optional expiration time.

    Parameters:
        user_id (int): The ID of the user.
        user_name (str): The name of the user.
        expiration_hours (int, optional): The number of hours until the token expires. Defaults to 1.

    Returns:
        str: The generated token.

    """
    current_time = datetime.datetime.utcnow()
    
    payload = {
        'user_id': user_id,
        'user_name': user_name,
        'iss': 'Issuer Name',
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
    """
    Validates the given token by decoding it using JWT.
    
    Args:
        token (str): The token to validate.
        pl (bool, optional): Flag indicating whether to return the payload of the token. 
                             Defaults to False.
    
    Returns:
        bool or dict: If `pl` is False, returns True if the token is valid, else False. 
                      If `pl` is True, returns the payload of the token if valid, else False.
    """
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'], verify=True, issuer='Issuer Name')
        
        print('\nValid Token\n')
        return True if not pl else payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        print('\nExpired Token\n')

        # Add new token request functionality

        return False
    except jwt.InvalidTokenError:
        # Invalid token
        print('\nInvalid Token\n')
        return False
