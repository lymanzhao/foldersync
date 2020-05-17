import os
from dirsync import sync
import multiprocessing
from multiprocessing import Manager

# sync("/Volumes/OSX2T/Down/于右任", "/Users/zhaoyunlai/Downloads/yu2", 'sync',)

def syncFile(sourcedirsync,targetdirsync):
    sync(sourcedirsync, targetdirsync, 'sync',)


if __name__ == "__main__":
    sourcedirsync = input("请输入要源文件夹：")
    try:
        # new_folder_name = old_folder_name + "[复件]"
        targetdirsync = input("请输入目标文件夹：")
        os.mkdir(targetdirsync)
    except:
        pass
    syncFile(sourcedirsync,targetdirsync)

    # pool = multiprocessing.Pool(2)
    # queue = Manager().Queue()
    # try:
    #     pool.apply_async(syncFile,args=(sourcedirsync,targetdirsync))
    #     pool.close()
    #     pool.join()
    # except:
	#     pool.terminate()
