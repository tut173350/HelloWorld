#ユーザからの入力を受け取り、出力する
message = input('Please input message:')
if message == 'gikadai': message = 'TUT'
output = 'Hello ' + message + '!'
print(output)
message = input('Please input second message:')
output = 'Hello ' + message + '!!'
print(output)
