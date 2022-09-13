safe_data='怉屰茓朘怘睭'
#这里是密文，也就是要进行暴力破译的密文
key=1000
#这里设置的是密钥的最大值，这里以1000为例子
#也就是说，密钥将会在1000-1 之间进行尝试

while key>0:
    data=''
    for y in safe_data:
        try:
            n=ord(y)-key
            n=chr(n)
            data=data+n
        except:
            pass
    print(str(key)+':'+str(data))
    print('')
    key=key-1
