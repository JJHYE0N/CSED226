# Problem 1
def factorial(n):
    # BEGIN_YOUR_CODE
    result = 1
    count = 0
    while n>0:
        result*=n
        n-=1
    #여기까지 팩토리얼 구현
    
    text = str(result)
    #to string 같은 역할
    
    #텍스트화시킴 reversed(text)로 뒤에서부터 읽고 0이면 count+1 아닐경우 break
    for word in reversed(text):
        if word=='0':
            count+=1
        else: break
    return count
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE

# Problem 2
def wordCount(filename):
    # BEGIN_YOUR_CODE
    with open(filename, encoding='cp949') as f:
        text = f.read().replace('\n', ' ')
    list = text.split()
    word_count = { }

    for word in list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE

# Problem 3
class car:
    def __init__(self, args):
        brand, model, price =  args
        self.brand = brand
        self.model = model
        self.price = price
def averagePrice(args):
    # BEGIN_YOUR_CODE (our solution is 10 lines of code, but don't worry if you deviate from this)
    i = len(args[0]) - 1
    count = 0
    result = 0
    #args[0][]는 왼쪽 입력값을 받아냄 KIA K5 5000 처럼
    #args[1]은 브랜드를 나타냄
    while i>=0:
        if (args[0][i].brand==args[1]):
            count+=1
            result += args[0][i].price
        i-=1
    if result>0:
        result/=count
    return result    
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE

# Problem 4
def distance(arr1, arr2):
    # BEGIN_YOUR_CODE
    import numpy as np
    #result = np.sqrt(np.sum(np.square(arr1 - arr2)))
    result = round(np.sqrt(np.sum(np.square(arr1 - arr2))), 2)
    return result
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE

# Problem 5
def pokemon(original_file, modified_file):
    # BEGIN_YOUR_CODE
    import pandas as pd
    from pandas import DataFrame
    
    #1) The processed csv file should not contain missing values; all rows with a missing value needs to be dropped.
    #2) The processed csv file should not contain columns 'Legendary', 'Sp. Atk', and 'Sp. Def'.
    #3) The processed csv file should only have Grass, Fire, Water, Normal 'Type 1' pokemons.
    #4) The processed csv file should only have rows where a value in 'Total' is greater than 200.
    #5) The processed csv file contains a new column named 'Power' where a value is 'strong' if Attack > 80 and 'week' otherwise.
    
    df1 = pd.read_csv(original_file)
    
    #1) missing value 행 제거
    df2 = df1.dropna(axis=0)
    
    #2) Legendary, Sp. Atk, and Sp. Def 제거
    df3 = df2.drop(['Legendary', 'Sp. Atk', 'Sp. Def'],axis=1)
    
    #3) Type 1에 Grass, Fire, Water, Normal만 유지 
    df4 = df3[df3['Type 1'].isin(["Grass","Fire","Water","Normal"])]
    #df4 = (df3['Type 1']=='Grass')|(df3['Type 1']=='Fire')|(df3['Type 1']=='Water')|(df3['Type 1']=='Normal')
    
    #4) Total is greater than 200
    df5 = df4[df4['Total']>200]
    
    #5) New column Power strong Attack > 80 otherwise weak
    df5 = df5.copy()
    df5['Power']=''
    for i, x in enumerate(df5['Attack']):
        df5.loc[df5['Attack'] > 80, 'Power'] = 'strong'
        df5.loc[df5['Attack'] <= 80, 'Power'] = 'weak'
    df = df5
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE
    df.to_csv(modified_file,index=False)

# Problem 6.a
def emp_table(dep, emp1, emp2):
    # BEGIN_YOUR_CODE (our solution is 7 lines of code, but don't worry if you deviate from this)
    import pandas as pd
    #from pandas import DataFrame
    
    df1 = pd.read_csv(dep)
    df2 = pd.read_csv(emp1)
    df3 = pd.read_csv(emp2)
    
    #concat axis=0 위아래로 합치기 
    #concat axis=1 좌우로 합치기
    emp = pd.concat([df2, df3], axis=0) 
    df4 = pd.merge(emp, df1)
    #df[df.drop(['employee_id', 'department_id'],axis=1)]
    df5 = df4.drop(['employee_id', 'department_id'],axis=1)
    df6 = df5.reindex(['name', 'salary', 'department_name'], axis = 1)
    #df[df.reindex(['name', 'salary', 'department_name'], axis = 1)]
    df = df6.sort_values('salary')
    #raise Exception("Not implemented yet")
    # END_YOUR_CODE
    return df  

# Problem 6.b
def lowest_avg(dep, emp1, emp2):
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    import pandas as pd
    #from pandas import DataFrame
    df0 = emp_table(dep, emp1, emp2)
    
    df = df0.groupby(['department_name'], as_index=False).mean()
    #print(df['salary'].idxmin())
    return df['department_name'][df['salary'].idxmin()]

    #raise Exception("Not implemented yet")
    # END_YOUR_CODE