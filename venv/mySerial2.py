"""
    Python应用开发——串口通信
    https://blog.csdn.net/ShenZhen_zixian/article/details/127397779?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-127397779-blog-116174534.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-127397779-blog-116174534.pc_relevant_default&utm_relevant_index=4
"""
# 导入模块
import threading
import time
import serial
import serial.tools.list_ports

# 自定义变量
port = "COM3"  # 端口号，根据自己实际情况输入，可以在设备管理器查看
bps = 9600     # 串口波特率，根据自己实际情况输入
timeout = 5       # 超时时间,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
rxdata = ''    # 接收的数据

# 扫描端口
def check_uart_port():
    port_list = list(serial.tools.list_ports.comports())
    # print(port_list)
    if len(port_list) == 0:
        print('can not fine uart port')
        return False
    else:
        for i in range(0,len(port_list)):
            print(port_list[i])
    return True

# 打开串口
def open_uart(port, bps, timeout):
    try:
        # 打开串口，并返回串口对象
        uart = serial.Serial(port, bps, timeout=timeout)
        return uart
    except Exception as result:
        print("can not open uart")
        print(result)
        return False

# 发送数据
def uart_send_data(uart, txbuf):
    len = uart.write(txbuf.encode('utf-8'))  # 写数据
    return len

# 接收数据
def uart_receive_data(uart):
    if uart.in_waiting:
        rxdata = uart.read(uart.in_waiting).decode("utf-8")   # 以字符串接收
        # rxdata = uart.read().hex()  # 以16进制(hex)接收
        print(rxdata)  # 打印数据

# 关闭串口
def close_uart(uart):
    uart.close()

# 创建一个线程用来等待串口接收数据
class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, uart):
        threading.Thread.__init__(self)
        self.uart = uart
    def run(self):                   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        while True:
            # print("thread_uart_receive")
            uart_receive_data(self.uart)  # 接收数据
            # time.sleep(0.01)

# 主函数
def main():
    # 扫描端口
    result = check_uart_port()
    if(result == False):
        return

    # 打开串口
    result = open_uart(port, bps, timeout)
    if (result == False):
        return
    else:
        uart1 = result

    # 创建一个线程用来接收串口数据
    thread_uart = myThread(uart1)
    thread_uart.start()

    while True:
        # 定时发送数据
        txbuf = "hello world"
        len = uart_send_data(uart1, txbuf)
        print("send len: ", len)
        time.sleep(1)

# 启动主函数
main()