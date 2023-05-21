questions=[["Which language was used to create fb?","Python","PHP","JS","NONE",4],["Which language was used to create fb?","Python","PHP","JS","NONE",1],
          ["Which language was used to create fb?","Python","PHP","JS","NONE",2],["Which language was used to create fb?","Python","PHP","JS","NONE",3],
           ["Which language was used to create fb?","Python","PHP","JS","NONE",1], ["Which language was used to create fb?","Python","PHP","JS","NONE",2],
            ["Which language was used to create fb?","Python","PHP","JS","NONE",3], ["Which language was used to create fb?","Python","PHP","JS","NONE",2],
            ["Which language was used to create fb?","Python","PHP","JS","NONE",4], ["Which language was used to create fb?","Python","PHP","JS","NONE",1],
            ["Which language was used to create fb?","Python","PHP","JS","NONE",3], ["Which language was used to create fb?","Python","PHP","JS","NONE",4],
           ["Which language was used to create fb?","Python","PHP","JS","NONE",1], ["Which language was used to create fb?","Python","PHP","JS","NONE",2],
            ["Which language was used to create fb?","Python","PHP","JS","NONE",3], ["Which language was used to create fb?","Python","PHP","JS","NONE",4]
          ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"THe question for Rupees{levels[i]}")
    print(f"a.{question[1]}               b.{question[2]}")
    print(f"c.{question[3]}               c.{question[4]}")
    reply = int(input("Enter the answer(1-4)"))
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs{levels[i]}")
        if(i==4):
            money=10000
        elif(i==10):
            money=320000
        elif(i==12):
            money=10000000
    else:
        print ("wrong answer")
        break
print(f"Your take home money is {money}")     