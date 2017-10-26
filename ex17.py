from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("从%s复制到%s" % (from_file, to_file))

# 我们也可以将这两行写成一行
in_file = open(from_file)
indata = in_file.read()

print ("indata的类型是", type(indata))
print ("输入的文件大小为%d字节" % len(indata))

print ("这个要输出的文件是不是已经存在？ %r" % exists(to_file))
print ("准备好就按回车键继续，或者按CTRL-C退出。")
input('>>>')

out_file = open(to_file, 'w')
out_file.write(indata)

print ("好了，搞定！")

out_file.close()
in_file.close()