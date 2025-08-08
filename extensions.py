
msg = input('File Name: ')
if '.jpg' in msg or '.jpeg' in msg:
    print('image/jpeg')
elif '.txt.pdf' in msg:
    print('application/pdf')
elif '.gif' in msg:
    print('image/gif')
elif '.png' in msg:
    print('image/png')
elif '.zip' in msg:
    print('application/zip')
elif '.txt' in msg:
    print('text/plain')
elif '.pdf' in msg or '.PDF' in msg:
    print('application/pdf')
elif '.bin' in msg or '.pdf' in msg:
    print('application/octet-stream')
else:
    print('application/octet-stream')
