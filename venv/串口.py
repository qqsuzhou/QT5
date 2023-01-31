"""
    python 串口通信
    注1：pip install pyserial
    注2：文件名字不能是serial.py，会和import serial冲突
    注3：官方的文档 https://pyserial.readthedocs.io/en/latest/
    https://blog.csdn.net/qq_17833651/article/details/127518999
    https://blog.csdn.net/FSgongzi/article/details/111935727?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-111935727-blog-127518999.pc_relevant_3mothn_strategy_and_data_recovery&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-111935727-blog-127518999.pc_relevant_3mothn_strategy_and_data_recovery&utm_relevant_index=1

"""

import serial  # 导入串口通信模块
import serial.tools.list_ports
from serial import PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE, STOPBITS_ONE, \
    STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
import re  # 提取文本中的特定类型字符

def get_serial():
    __plist = list(serial.tools.list_ports.comports())
    __ports = [p.name for p in __plist]
    return __ports

def conn_serial():
# 创建串口对象
    ser = serial.Serial(port="COM5", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1, rtscts=False)

    # 判断串口是否打开
    if ser.isOpen():
        print('open success.')

        # 发送数据，这里只支持 bytes 类型的数据，需要对字符串进行 encode 编码
        # send_len = ser.write(b'usb start')
        # print('send data length: {}'.format(send_len))

        # 读取数据，读取的内容也是 bytes 类型
        read_msg = ser.readline()
        print('read_msg: {}'.format(read_msg))

    else:
        print('open failed.')

    # 关闭串口
    ser.close()

myPorts=get_serial()
print(myPorts)
conn_serial()




