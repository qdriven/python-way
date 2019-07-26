# -*- coding: utf-8 -*-
from swagger_parser import SwaggerParser

parser = SwaggerParser(swagger_path='https://petstore.swagger.io/v2/swagger.json')

print(parser)

