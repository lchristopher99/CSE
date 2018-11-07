ID_obj = {
  'format' : ('Name: ', 'Age: ', 'Major: '),
  'clc1085' : ('Logan Christopher', '18', 'Computer Science'),
  'abc1234' : ('John Smith', '17', 'Marketing')
}

netID = input('Enter Net ID: ')

for i in range(0,3):
  print(ID_obj['format'][i], end='')
  print(ID_obj[netID][i])