'''
这个文件是基于SafeChat3.0所改编的
用于适配GUI
___________用法___________
只有两个函数：
encrypt ->> 加密
decrypt ->> 解密
另外虽然本函数是为维吉尼亚加密法设计的，但是当做普通的凯撒加密也是可以的！只要key为一个字母即可
'''
def encrypt(Data_Unsafe='',Key_Input=''):   # 加密
    finally_output=''
    Data_Unsafe_List = []
    Key_List = []  # 密钥列表（字母）
    Key_USE_LIST = []  # 密钥列表（最终数字）
    Data_Safe_List = []

    # 把用户输入的 文字密钥和原文 变列表
    for i in Key_Input:  # Key_Input 转 Key_List 列表
        Key_List.append(i)
    for i in Data_Unsafe:  # Data_Unsafe 转 Data_Unsafe_List
        Data_Unsafe_List.append(i)
    # for i in Data_Unsafe2:
    # Data_Unsafe_List2.append(i)

  # 文字密钥 变 数字密钥 并创列表
    num1 = 0
    num2 = len(Key_List)
    while num1 < num2:
        data = Key_List[num1]  # 把key_input中的字母一个个剥离开进行处理
        a = ReTurnToKey(data)  # 将单个字母变为单个Key_USE
        # print(str(a))
        num1 = num1 + 1
        Key_USE_LIST.append(a)  # 处理完成后添加进list里，做最终使用的准备

    key_num = len(Key_USE_LIST)  # 密钥位数
    x = 0
    data_num = len(Data_Unsafe_List)
    data_num2 = len(Data_Unsafe_List)  # 要加密的位数
    y = 0
    while data_num > 0:
        if x <= key_num - 1:
            if y <= data_num2:
                a = Data_Unsafe_List[y]
                a = ord(a)
                b = a + int(Key_USE_LIST[x])
                Data_Safe_List.append(chr(b))
                x += 1
                y += 1
                data_num -= 1

        else:
            if x > key_num - 1:
                x = 0
    for i in Data_Safe_List:
        finally_output=finally_output+str(i)
    return finally_output

def decrypt(Data_Safe='',Key_Input=''): # 解密
    finally_output='' # 最终输出
    Data_Safe_List = []
    Key_List = []  # 密钥列表（字母）
    Key_USE_LIST = []  # 密钥列表（最终数字）
    Data_Unsafe_List2_Output = []


      # 把用户输入的 文字密钥和原文 变列表
    for i in Key_Input:  # Key_Input 转 Key_List 列表
        Key_List.append(i)
    # for i in Data_Unsafe2:
    # Data_Unsafe_List2.append(i)
    for i in Data_Safe:
        Data_Safe_List.append(i)
      # 文字密钥 变 数字密钥 并创列表
    num1 = 0
    num2 = len(Key_List)
    while num1 < num2:
        data = Key_List[num1]  # 把key_input中的字母一个个剥离开进行处理
        a = ReTurnToKey(data)  # 将单个字母变为单个Key_USE
        # print(str(a))
        num1 = num1 + 1
        Key_USE_LIST.append(a)  # 处理完成后添加进list里，做最终使用的准备

    key_num = len(Key_USE_LIST)  # 密钥位数
    x = 0
    data_num = len(Data_Safe_List)
    data_num2 = len(Data_Safe_List)  # 要解密的位数
    y = 0
    while data_num > 0:
        if x <= key_num - 1:
            if y <= data_num2:
                a = Data_Safe_List[y]
                a = ord(a)
                b = a - int(Key_USE_LIST[x])
                Data_Unsafe_List2_Output.append(chr(b))
                x += 1
                y += 1
                data_num -= 1
        else:
            if x > key_num - 1:
                x = 0
    for f in Data_Unsafe_List2_Output:
        finally_output=finally_output+str(f)
    return finally_output

def ReTurnToKey(letter):  # 这个模块可以将 密钥中的字母 转为 用于加密的数字
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
