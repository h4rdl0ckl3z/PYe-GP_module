# PYe-GP_module (Thai e-Government Procurement)
## python ≥ 3.8
### example
```
print(e_GP(['egpid']))
```
or
```
from e_GP import e_GP
print(e_GP(['egpid']))
```
### json to csv
```
from e_GP import e_GP
data = e_GP(['egpid'])

import pandas as pd
import json

json_data = json.loads(data)
df = pd.DataFrame(json_data)
df.to_csv('output.csv', index=False)
```

![image](https://github.com/user-attachments/assets/3b9da0b8-515e-4613-8bac-c37057c16d7c)



### lookuperror unknown encoding windows-874 (fixed)
