# import pandas as pd

# s = pd.Series([10,20,30,40,50,60],name="mark")
# print(s)
#Mathmatic function
# s = pd.Series([10,20,30,40,50,60],name="mark")
#Mathmatic function
# print(s+5)#add
# print(s-5)#subtrac
# print(s/5)#"divide"
# print(s*2)# multipecation
# print(s**2)
# Arthmatic function
# print(s.sum())
# print(s.min())
# print(s.max())
# print(s.count())
# print(s.std())
 


# s_var =pd.Series([70,80,90,40,50,60],["a","b","c","d","e","f"])
# print(s_var)


# DATAFRAME
# import pandas as pd

# Data ={
#     "name":["shubham","karan","rashed","bhupathi"],
#     "age":[20,21,21,30],
#     "city":["pandherpur","vasai","bhiwande","kerala"],
#     "college":"vcet",
#     "mark":[80,89,90,99]

# }

# df = pd. DataFrame(Data)
# print(df.tail())
# print(df.head())

import pandas as pd

Data ={
    "name":["shubham","karan","rashad"],
    "age":[10,22,30],
    "city":["mumbia","vasia","bhewande"]
}

df =pd.DataFrame(Data)
# df["age"]=df["age"]+2  #update value
# df.loc[2,"city"]= "waet vasai"
# df.iloc[0,2]="pandherpur"
# print(df)

#creat file csv
df.to_csv("friend.csv",index=False)
print("creat file csv succese ful")


# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.index)
# print(df.dtypes)

#read file 

# import pandas as pd

# df = pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\sample-simple.csv")
# # df =open(r"C:\Users\Asus\OneDrive\Desktop\python\Data-engineer-python-sql-\python2\sample-simple.csv","r")
# # print(df.read())
# # df.close()
# print(df)