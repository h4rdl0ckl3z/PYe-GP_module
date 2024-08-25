# PYe-GP_module (Thai Government Procurement)
## python ≥ 3.8
### example
```
print(e_GP(['egpid']))
```
### or
```
from e_GP import e_GP
print(e_GP(['egpid']))
```
![image](https://github.com/user-attachments/assets/f720c505-6e8c-413c-a7eb-cd3822215c44)


### How to fixed : lookuperror unknown encoding windows-874 (fixed)
Windows -> C:\Users\\[username]\AppData\Local\Programs\Python\Python[version]\Lib\encodings

Linux -> /usr/lib/python[version]/encodings/ or /usr/lib64/python[version]/encodings/

Edit aliases.py

```
# cp874 codec
'874'                : 'cp874',
'windows_874'        : 'cp874',
```

###### JavaScript
###### https://github.com/h4rdl0ckl3z/JSe-GP_module


Discord -> https://discord.gg/tDdse2UYwZ
