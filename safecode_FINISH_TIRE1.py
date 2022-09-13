def safe(data,key):
    safe_data=''
    for s in data:
        a=ord(s)
        b=a+key
        safe_data=safe_data+chr(b)
    print('加密后的密文为:'+str(safe_data))
    print('请妥善保管密钥:'+str(key))
def break_down(safe_data,key):
    data=''
    for y in safe_data:
        n=ord(y)-key
        n=chr(n)
        data=data+n
    print('解密后原文为:'+str(data))


cheak=''
while cheak != 'q':
    print('''
    1.加密原文
    2.解密密文
    （回复q退出）
    ''')
    cheak=input('请输入操作：')
    try:
        if cheak=='1':
            print('您选择了项目一，加密原文')
            data=str(input('请输入原文：'))
            key=int(input('请输入密钥：'))
            safe(data, key)
        elif cheak=='2':
            print('你选择了项目二，解密密文')
            safe_data=str(input('请输入密文：'))
            key=int(input('请输入密钥：'))
            break_down(safe_data,key)
    except:
        print('出错！')
        pass