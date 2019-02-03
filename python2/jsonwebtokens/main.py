import base64
import hashlib
import hmac
import json
import re
from collections import OrderedDict

def get_jwt(header, payload):
	header_b64_url_encoded = base64.b64encode(re.sub(r'\s+', '', json.dumps(header)))
	payload_b64_url_encoded = base64.b64encode(re.sub(r'\s+', '', json.dumps(payload)))

	print 'HEADER', header_b64_url_encoded
	print 'PAYLOAD', payload_b64_url_encoded 

	msg = header_b64_url_encoded + '.' + payload_b64_url_encoded
	hmac_signed = hmac.new('secret', msg=msg, digestmod=hashlib.sha256).hexdigest()
	signature = base64.b64encode(hmac_signed)
	
	jwt = msg + '.' + signature
	return jwt


if __name__ == "__main__":
	header = OrderedDict(
		typ= 'JWT',
		alg= 'HS256'
	)

	payload = {
		'user_id': 'a1b2c3-x11y22z33-sbi-user-12',
		'is_admin': 'yes'
	}

	jwt = get_jwt(header, payload)
	print(jwt)

