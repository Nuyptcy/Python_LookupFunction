# -*- coding: utf-8 -*-

#Step1匯入自備餐具優惠餐廳csv檔
import csv
print("""
全台各地自備餐具與飲料袋享優惠之餐廳統計表

輸入0離開程式    
輸入1查看餐廳優惠方式比例
輸入2查看優惠方式為集點之餐廳
輸入3查看優惠方式為折價之餐廳
輸入4查看優惠方式為贈送餐飲之餐廳
選擇查詢內容:
""")
#Step2讀取資料
#fn1 = r'C:\Allie\FinalProject\OwnedCutlery.csv'
fn1 = r'/Users/aichung/Desktop/final_project/OwnedCutlery.csv'
with open(fn1,encoding='utf8') as csvFile:
    csvReader = csv.reader(csvFile)
    cutleryData = list(csvReader)
    #print(cutleryData)
#Step3撈出資料並統計
#Step4 import plt以圖示比例
    
import matplotlib.pyplot as plt 

GBType = list(set([cutleryData[i][7] for i in range(1,len(cutleryData))]))
count = [0]*len(GBType)#list 
supplierName = list(set(cutleryData[i][1] for i in range(1,len(cutleryData))))
#整理完的labels

for i in range(1,len(cutleryData)):
    count[GBType.index(cutleryData[i][7])]+=1
#GBType = [[GBType[i],count[i]]for i in range(len(GBType))]


'''
while True:
    keyin =eval(input())
    if keyin ==0:
        print('Bye')
        break;
    elif keyin ==1:
        x = GBType#x = labels
        y = count
        plt.title('餐廳優惠方式統計表')
        plt.pie(y,labels=x, autopct="%1.1f%%")
        plt.show()
    elif keyin ==2:
        for i in range(1,len(cutleryData)):
            if '集點' in cutleryData[i][7]:
                print(cutleryData[i][1])
    elif keyin ==3:
        for i in range(1,len(cutleryData)):
            if '折價' in cutleryData[i][7]:
                print(cutleryData[i][1])
    elif keyin ==4:
        for i in range(1,len(cutleryData)):
            if '贈送餐飲' in cutleryData[i][7]:
                print(cutleryData[i][1])
    else:
        print('輸入錯誤')  
'''

while True:
    keyin =eval(input())
    if keyin ==0:
        print('Bye')
        break;
    elif keyin ==1:
        x = GBType#x = labels
        y = count
        plt.title('餐廳優惠方式統計表')
        plt.pie(y,labels=x, autopct="%1.1f%%")
        plt.show()
    elif keyin ==2:
        for i in range(1,len(cutleryData)):
            if '集點' in cutleryData[i][7]:
                print(cutleryData[i][1])
    elif keyin ==3:
        for i in range(1,len(cutleryData)):
            if '折價' in cutleryData[i][7]:
                print(cutleryData[i][1])
    elif keyin ==4:
        for i in range(1,len(cutleryData)):
            if '贈送餐飲' in cutleryData[i][7]:
                print(cutleryData[i][1])
    else:
        print('輸入錯誤')        
         

