# import oss2
# import os

# def oss_up_cb(up_size, total_size):
# 	print(up_size, total_size)
	
# if __name__ == '__main__':
# 	access_key_id = 'LTAI4GJq5fpr5LfUggyDLFDc'
# 	access_key_secret = 'bTCHF7tSboJUfcZsXxWeHkP3sz64yS'
# 	endpoint = 'http://oss-cn-beijing.aliyuncs.com'
# 	bucket_name = 'picture-fashion'
# 	project_dir = 'game/linxinfa/'
# 	bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name=bucket_name)
# 	for f in oss2.ObjectIterator(bucket, project_dir):
# 	    # 文件名
# 	    fpath= f.key
# 	    print(fpath)
	    # 删除
	    # bucket.delete_object(fpath)
	    # 下载
	    # local_dir = 'D://oss/downloadtest/'
	    # fname = os.path.basename(fpath)
	    # if '' != fname:
	    # 		bucket.get_object_to_file(fpath, local_dir + os.path.basename(fpath))
	# 上传
	# local_f = 'test.txt'
	# cloud_f = project_dir + local_f
	# bucket.put_object_from_file(cloud_f, local_f, progress_callback = oss_up_cb)


import oss2
import os
import time
def upload_oss_file():
    endpoint = 'http://oss-cn-beijing.aliyuncs.com'
 
    auth = oss2.Auth('LTAI4GJq5fpr5LfUggyDLFDc', 'bTCHF7tSboJUfcZsXxWeHkP3sz64yS')
    bucket = oss2.Bucket(auth, endpoint, 'picture-fashion')
    directory = r'/Users/akirachang/Desktop/175990_396802_bundle_archive/images/'
    index = 0
    for entry in os.scandir(directory):
        if (entry.path.endswith(".jpg") or entry.path.endswith(".png")) and entry.is_file():
            print(entry.name)
            bucket.put_object_from_file(entry.name, entry.path)
            index+=1
    # 上传
upload_oss_file()
