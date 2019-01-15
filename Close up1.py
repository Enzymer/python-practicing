Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(sys.version)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(sys.version)
NameError: name 'sys' is not defined
>>> import sys
>>> sys.platform
'win32'
>>> print(sys.version)
3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)]
>>> import os
>>> os.getcwd()
'C:\\Users\\Toshi\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Toshi\\AppData\\Roaming', 'ASL.LOG': 'Destination=file', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'TOSHIKI', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'CONFIGSETROOT': 'C:\\WINDOWS\\ConfigSetRoot', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'FP_NO_HOST_CHECK': 'NO', 'HOME': 'C:\\Users\\Toshi', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Toshi', 'LOCALAPPDATA': 'C:\\Users\\Toshi\\AppData\\Local', 'LOGONSERVER': '\\\\TOSHIKI', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\Toshi\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\Toshi\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\Toshi\\AppData\\Local\\Programs\\Python\\Python36-32\\;C:\\Users\\Toshi\\AppData\\Local\\Microsoft\\WindowsApps;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 69 Stepping 1, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '4501', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\Toshi\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\Toshi\\AppData\\Local\\Temp', 'USERDOMAIN': 'TOSHIKI', 'USERDOMAIN_ROAMINGPROFILE': 'TOSHIKI', 'USERNAME': 'Toshi', 'USERPROFILE': 'C:\\Users\\Toshi', 'WINDIR': 'C:\\WINDOWS'})
>>> os.getenv('APPDATA')
'C:\\Users\\Toshi\\AppData\\Roaming'
>>> import datetime
>>> datetime.date.today()
datetime.date(2018, 6, 22)
>>> datetime.date.today() .day
22
>>> datetime.date.today() .month
6
>>> datetime.date.today() .year
2018
>>> datetime.date.isoformat(datetime.date.today())
'2018-06-22'
>>> import time
>>> time.strftime("%H:%M")
'15:03'
>>> time.strftime("%A:%P")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    time.strftime("%A:%P")
ValueError: Invalid format string
>>> time.strftime("%A %P")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    time.strftime("%A %P")
ValueError: Invalid format string
>>> time.strftime("%A %p")
'Friday PM'
>>> import html
>>> html.escape("This HTML fragment contains a <script>script</script> tag.")
'This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'
>>> html.unescape("I &hearts; Python's &lt;standard library&gt;.")
"I ♥ Python's <standard library>."
>>> 
=================== RESTART: C:\Users\Toshi\Desktop\odd.py ===================
分の値は奇数。
>>> 
=================== RESTART: C:\Users\Toshi\Desktop\odd.py ===================
分の値は奇数。
>>> for i in [1,2,3]:
	print(i)

	
1
2
3
>>> for ch in "Hi!":
	print(ch)

	
H
i
!
>>> for num in range(5):
	print('Head First Rocks')

	
Head First Rocks
Head First Rocks
Head First Rocks
Head First Rocks
Head First Rocks
>>> 
=================== RESTART: C:\Users\Toshi\Desktop\odd.py ===================
分の値は奇数ではない。

=================== RESTART: C:\Users\Toshi\Desktop\odd.py ===================
分の値は奇数ではない。
分の値は奇数。
分の値は奇数ではない。
分の値は奇数ではない。
分の値は奇数ではない。
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> 
