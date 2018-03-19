from gmail import GMail,Message
from random import choice
import datetime
import time

gmail=('nhihcb.fyu@gmail.com','0906698033')

html_template="""
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p></p>
<p>Em ch&agrave;o thầy</p>
<p>Em l&agrave; <span style="color: #ff99cc;">Bảo Nhi</span></p>
<p>H&ocirc;m nay em {{sick}} muốn đi shopping n&ecirc;n xin thầy cho em nghỉ 1 buổi</p>
<p></p>
<p>Thương y&ecirc;u</p>
<p>Bảo Nhi</p>
<p></p>
"""

reasons = ['đau bụng','đau đầu','mẹ em kêu ở nhà']
reason = choice(reasons)
html_new = html_template.replace('{{sick}}',reason)

msg = Message('Test Message',
to='teckidsc4e16@gmail.com',
html=html_new)

now = datetime.datetime.now()
sent = False
while not sent:
    if now.hour==7:
        gmail.send(msg)
        sent = True
    else:
        time.sleep(10)
