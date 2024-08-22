# python ≥ 3.8
# example
```
print(e_GP(['egpid']))
```
## or
```
from e_GP import e_GP
print(e_GP(['egpid']))
```
![image](https://github.com/user-attachments/assets/fec9e92b-df35-4514-b326-7c4f315a419c)


### How to fixed : lookuperror unknown encoding windows-874 (fixed)
Windows -> C:\Users\\[username]\AppData\Local\Programs\Python\Python[version]\Lib\encodings

Linux -> /usr/lib/python[version]/encodings/ or /usr/lib64/python[version]/encodings/

Edit aliases.py

```
# cp874 codec
'874'                : 'cp874',
'windows_874'        : 'cp874',
```
