#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def general_space2randomblank(payload):
	# -- general -- #
	_payload = payload
	blanks = ('%09','%0A','%0C','%0D')

	if payload:
		_payload = ""
		quote,doublequote,firstspace = False,False,False
		for i in range(len(payload)):
			if not firstspace:
				if payload[i].isspace():
					firstspace = True
					_payload += random.choice(blanks)
					continue
			elif payload[i] == '\'':
				quote = not quote
			elif payload[i] == '"':
				doublequote = not doublequote
			elif payload[i] == ' ' and not doublequote and not quote:
				_payload += random.choice(blanks)
				continue
			_payload = payload[i]
	return _payload