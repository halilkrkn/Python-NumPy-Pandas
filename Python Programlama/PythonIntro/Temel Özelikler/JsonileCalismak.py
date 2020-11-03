# -*- coding: utf-8 -*-

import json as js

data = '{"firstName":"Halil", "lastName":"Karkin"}'

y = js.loads(data)

print("\n" + y["firstName"] + y["lastName"])

customer = {
        "fistName":"Musa",
        "lastName":"Karkın",
        "email":"mskrkn@gmail.com"
        }

#js.dumps ile customer sözlüğünü json formatına çevirdik
customerJson = js.dumps(customer)
print(customerJson)

