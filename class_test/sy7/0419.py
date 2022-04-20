scores = []												# 创建空列表，用于储存从文本文件中读取的成绩信息
txtfilepath = 'data.txt'
with open(txtfilepath, 'r',encoding='utf-8') as f:			# 打开文件
    for s in f.readlines():								# 读取并遍历文件行
       scores.append(int(s))
result_filepath = 'result.txt'
with open(result_filepath,'w', encoding='utf-8') as f:	# 打开文件
    f.write("成绩个数：{}\n".format(len(scores)))
    f.write("最高分：{}\n".format(max(scores)))
    f.write("最低分：{}\n".format(min(scores)))
    f.write("平均分：{}\n".format(sum(scores)/len(scores)))
print("成绩个数：{}".format(len(scores)))
print("最高分：{}".format(max(scores)))
print("最低分：{}".format(min(scores)))
print("平均分：{}".format(sum(scores)/len(scores)))