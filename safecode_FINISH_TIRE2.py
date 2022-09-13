'''safecode 2.0版本加密内容
    在进行加密之前先对字符串进行反转，防止针对凯撒密码进行暴力破解'''

def safe(data,key):
    
    #将明文生成密文（data-tire1)
    safe_data_1='' 
    for s in data:
        a=ord(s)
        b=a+key
        safe_data_1=safe_data_1+chr(b)
    
    #进行密文的倒序生成(tire1-tire2)
    i=len(safe_data_1)
    safe_data_2=''  
    while i>0:
        safe_data_2=safe_data_2+safe_data_1[i-1]
        i=i-1
    
    #print('加密后tire 1 密文为:'+str(safe_data_1)) 
    #此行代码为未经倒序的密文，仅用于编写测试
    
    print('加密后 tire2级别 密文为：'+str(safe_data_2))
    print('请妥善保管密钥:'+str(key))


def break_down(safe_data_2,key):
    
    #进行密文的顺序还原(tire2-tire1)
    i=len(safe_data_2)
    safe_data_1=''  
    while i>0:
        safe_data_1=safe_data_1 + safe_data_2[i-1]
        i=i-1
    data=''
    #解密为原文（tire1-data）
    for y in safe_data_1:
        n=ord(y)-key
        n=chr(n)
        data=data+n
    #print('经过tire1算法 解密后原文为:'+str(safe_data_1))
    #此行代码为重新排序的密文文，仅用于编写测试
    print('经过tire2算法 解密后原文为:'+str(data))


cheak=''
while cheak != 'q':
    print('''
    1.加密原文
    2.解密密文
    回复q退出
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