from logging import exception


def print_file_info(file_name):
    try:
        r=open("file_name","r",encoding="UTF-8")
    except:
        print("读取文件失败")
    else:
        print(r.read())
    finally:
        r.close()
def append_to_file(file_name,data):
    a=open("file_name","a",encoding="utf-8")
    a.write(data)
    a.flush()

