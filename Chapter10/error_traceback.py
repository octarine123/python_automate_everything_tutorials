Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/pi/auto_python_chp10_2.py", line 10, in <module>
    spam()
  File "/home/pi/auto_python_chp10_2.py", line 5, in spam
    bacon()
  File "/home/pi/auto_python_chp10_2.py", line 8, in bacon
    raise Exception('This is an error message')
Exception: This is an error message
>>> import traceback
>>> try:
	raise Exception('This is an error message')
except:
	errorFile = open('errorInfo.txt','w')
	errorFile.write(traceback.format_exec())
	errorFile.close()
	print('The traceback was written to errorInfo.txt')

	
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    raise Exception('This is an error message')
Exception: This is an error message

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#8>", line 5, in <module>
    errorFile.write(traceback.format_exec())
AttributeError: 'module' object has no attribute 'format_exec'
>>> >>> try:
	raise Exception('This is an error message')
except:
	errorFile = open('errorInfo.txt','w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback was written to errorInfo.txt')
	
SyntaxError: invalid syntax
>>> try:
	raise Exception('This is an error message')
except:
	errorFile = open('errorInfo.txt','w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback was written to errorInfo.txt')

	
114
The traceback was written to errorInfo.txt
>>> 
