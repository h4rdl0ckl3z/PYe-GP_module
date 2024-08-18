# example
```
print(e_GP(['egpid']))
```
## or
```
import e_GP
print(e_GP(['egpid']))
```

### How to fixed : lookuperror unknown encoding windows-874
Windows -> C:\Users\[username]\AppData\Local\Programs\Python\Python[version]\Lib\encodings

Linux -> /usr/lib/python[version]/encodings/ or /usr/lib64/python[version]/encodings/

Edit aliases.py

```
# cp874 codec
'874'                : 'cp874',
'windows_874'        : 'cp874',
```
