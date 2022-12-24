# import csv
import pandas as pd



# with open("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/pandas and csv file/wheather_data.csv") as file:
#     data=csv.reader(file)  
#     temperature=[]
#     for rows in data:    
#         if rows[1]!="temp":
#             temperature.append(int(rows[1]))
#     print(temperature)
     


data=pd.read_csv("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/pandas and csv file/wheather_data.csv")
mon_data=data[data.day=="Monday"]
# print(mon_data)

# print(data[data.temp==data.temp.max()])




# print(data.condition)



# print(type(data))
# temp_list=(data["temp"]).max()

# print(temp_list)



# summed_temp=sum(temp_list)
# print(summed_temp/len(temp_list))


# dict_data=data.to_dict()
# print(dict_data)

#cratinng a dataframe from a dictiobary

# data_dic={
#     "student": ["Amy", "James", "Angela"],
#     "scores":[76,56,65]
# }
# data=pd.DataFrame(data_dic)
# data.to_csv("new_csv_data")


