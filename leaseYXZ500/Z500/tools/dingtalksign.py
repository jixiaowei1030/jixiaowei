import time
import hmac
import hashlib
import base64
import urllib.parse


def dingtalksign():
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC0bcc0e49cc6b99f9ddb5e978071fa6b509b3bf592bdf64d82a605e2a2eb6ae0a'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign
