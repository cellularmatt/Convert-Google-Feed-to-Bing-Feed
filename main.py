import get_xml as get
import edit_xml as edit
import convert_xml as convert
import upload_xml as upload
import time
from datetime import datetime

now = datetime.now()
month = now.month
day = now.day
year = now.year
hour = now.hour
minute = now.minute
second = now.second
micsec = now.microsecond

print('#'*20)
print('Started script on: '+ str(month) + '/'+ str(day) + '/'+ str(year) + ' '+ str(hour) + ':'+ str(minute) + ':'+ str(second) + ':' + str(micsec) )
print('#'*20)
start = time.time()

get.get_xml()
edit.edit_xml()
convert.convert_xml()
upload.upload_xml()

end = time.time()
print('Script took ' + str(end - start) + ' seconds to run!\n\n')
print('#'*20)
