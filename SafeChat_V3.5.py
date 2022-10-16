
import time
Data_Unsafe = str(input('请输入原文，没有可留空：'))# 原文
Data_Unsafe_List = []
Data_Unsafe_NUM=len(Data_Unsafe)


Data_Safe = str(input('请输入密文，没有可留空：'))  # 密文
Data_Safe_List = []

Data_Unsafe_List2_Output=[] #密文转明文

print('v3.5版本温馨提示：一次一密加密法需要密文和原文同等大小 如果您在解密消息，请确认密钥完整且正确')
time.sleep(1)
print('需要的密文长度（解密者忽略此消息）:'+str(Data_Unsafe_NUM))
Key_Input = str(input('请输入密钥，必填：'))# 密钥（用户输入）
while len(Key_Input) < len(Data_Unsafe):
    print('不符合要求')
    Key_Input = str(input('请输入密钥，必填：'))
Key_List = []  # 密钥列表（字母）
Key_USE_LIST = []  # 密钥列表（最终数字）


def ListInit():
    for i in Key_Input:  # Key_Input 转 Key_List 列表
        Key_List.append(i)
    for i in Data_Unsafe:  # Data_Unsafe 转 Data_Unsafe_List
        Data_Unsafe_List.append(i)
    #for i in Data_Unsafe2:
        #Data_Unsafe_List2.append(i)
    for i in Data_Safe:
        Data_Safe_List.append(i)

def ReTurnToKey(letter):  # 这个模块可以将 密钥中的字母 转为 用于加密的数字
    global key
    letter = letter.upper()
    # print(letter)
    if letter == 'A':
        key = 1
    elif letter == 'B':
        key = 2
    elif letter == 'C':
        key = 3
    elif letter == 'D':
        key = 4
    elif letter == 'E':
        key = 5
    elif letter == 'F':
        key = 6
    elif letter == 'G':
        key = 7
    elif letter == 'H':
        key = 8
    elif letter == 'I':
        key = 9
    elif letter == 'J':
        key = 10
    elif letter == 'K':
        key = 11
    elif letter == 'L':
        key = 12
    elif letter == 'M':
        key = 13
    elif letter == 'N':
        key = 14
    elif letter == 'O':
        key = 15
    elif letter == 'P':
        key = 16
    elif letter == 'Q':
        key = 17
    elif letter == 'R':
        key = 18
    elif letter == 'S':
        key = 19
    elif letter == 'T':
        key = 20
    elif letter == 'U':
        key = 21
    elif letter == 'V':
        key = 22
    elif letter == 'W':
        key = 23
    elif letter == 'X':
        key = 24
    elif letter == 'Y':
        key = 25
    elif letter == 'Z':
        key = 26
    return key


def MakeAKeyList():  # 将 加密的数字 转为 列表
    num1 = 0
    num2 = len(Key_List)
    while num1 < num2:
        data = Key_List[num1]  # 把key_input中的字母一个个剥离开进行处理
        a = ReTurnToKey(data)  # 将单个字母变为单个Key_USE
        # print(str(a))
        num1 = num1+1
        Key_USE_LIST.append(a)  # 处理完成后添加进list里，做最终使用的准备


def Safe():  # 对文本进行加密
    key_num = len(Key_USE_LIST)  # 密钥位数
    x = 0
    data_num = len(Data_Unsafe_List)
    data_num2 = len(Data_Unsafe_List)   # 要加密的位数
    y = 0
    while data_num > 0:
        if x <= key_num-1:
            if y <= data_num2:
                a = Data_Unsafe_List[y]
                a = ord(a)
                b = a+int(Key_USE_LIST[x])
                Data_Safe_List.append(chr(b))
                x += 1
                y += 1
                data_num -= 1

        else:
            if x > key_num-1:
                x = 0


def UnSafe(): #对文本进行解密
    key_num = len(Key_USE_LIST)  # 密钥位数
    x = 0
    data_num = len(Data_Safe_List)
    data_num2 = len(Data_Safe_List)   # 要解密的位数
    y = 0
    while data_num > 0:
        if x <= key_num-1:
            if y <= data_num2:
                a = Data_Safe_List[y]
                a = ord(a)
                b = a-int(Key_USE_LIST[x])
                Data_Unsafe_List2_Output.append(chr(b))
                x += 1
                y += 1
                data_num -= 1
        else:
            if x > key_num-1:
                x = 0


def encrypt():
    ListInit()  # 把用户输入的 文字密钥和原文 变列表
    MakeAKeyList()  # 文字密钥 变 数字密钥 并创列表
    Safe()
    for i in Data_Safe_List:
        print(i, end='')


def decrypt():
    ListInit()  # 把用户输入的 文字密钥和原文 变列表
    MakeAKeyList()  # 文字密钥 变 数字密钥 并创列表
    UnSafe()
    for f in Data_Unsafe_List2_Output:
        print(f, end='')
    








    # 加密方法：
    #ListInit()  # 把用户输入的 文字密钥和原文 变列表
    # MakeAKeyList()  # 文字密钥 变 数字密钥 并创列表
    # Safe()  # 加密
    # UnSafe()
    #decrypt()
    #encrypt()
    #print(Data_Safe_List)
    

t=1
while t > 0 :
    print('''
    1.加密
    2.解密
    ''')
    time.sleep(1)
    choice=int(input('请选择：'))
    if choice==1:
        encrypt()
        t -=1
    elif choice==2:
        decrypt()
        t-=1
    else:
        print('选项不存在')

        #ABCDEFGHIJKLMNOPQRSTUVMXYZabcdefghijklmnopqrstuvwxyz1234567890
        
