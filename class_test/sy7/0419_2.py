import csv

scores = []									# 创建空列表，用于储存从csv文件中读取的成绩信息
csvfilepath = 'data.csv'
with open(csvfilepath, newline='') as f:	# 打开文件
	f_csv = csv.reader(f)					# 创建csv.reader对象
	headers = next(f_csv)   				# 标题
	for row in f_csv:						# 循环打印各行（列表）
		scores.append(row)
print("原始记录:",scores)
scoresData = []
for rec in scores:
    scoresData.append(int(rec[2]))
print("成绩列表:",scoresData)
print("平均成绩:",sum(scoresData)/len(scoresData))
