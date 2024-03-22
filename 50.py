a="Peace be upon You"
print(str(a))
print(repr(a))

c=eval(repr(a))#(eval)This is built in function  and used for convert argument into mathematical function

if a==c:
    print("both b and c are same")