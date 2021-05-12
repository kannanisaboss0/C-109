#--------------------------------------------------------------PerformanceResult.py--------------------------------------------------------------#

'''
Importing modules:
-pandas (pd)
-plotly.figure_factory (ff)
-plotly.graph_objects (go)
-csv
-statistics
-time
'''
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import time

#Defining a function for converting a specefic dataframe to list
def ConvertDataframeToList(dataframe_arg):
    list_result=list(dataframe_arg)
    return list_result

#Defining a function to ask the user whether to categorise further or not
def VerifyCategorisation():
  function_input=input("Continue further categorisation?(:-Yes or No)")
  if(function_input=="Yes"):
    return "Yes"
  else:
    return "No"  

#Defining a function for finding the modes,median,mean and standard deviation for thegiven list   
def ModifyDataframeAndGenerateGraph(choice_arg,parameter):
  
    #Creating the graph and finiding mode,median,mean and standarad deviation
    subject_param_df=subject_df.loc[df[parameter]==choice_arg]
    subject_param_list=ConvertDataframeToList(subject_param_df) 
    list_mean=statistics.mean(subject_param_list)
    list_st_dev=statistics.stdev(subject_param_list)
    list_mode=statistics.mode(subject_param_list)
    list_median=statistics.median(subject_param_list)

    #Categorising the standard deviation
    st_dev_start_1,st_dev_end_1=list_mean-(1*list_st_dev),list_mean+(1*list_st_dev)
    st_dev_start_2,st_dev_end_2=list_mean-(2*list_st_dev),list_mean+(2*list_st_dev)
    st_dev_start_3,st_dev_end_3=list_mean-(3*list_st_dev),list_mean+(3*list_st_dev)

    #Categorising the data according to standard deviation
    st_dev_1_range=[result_1 for result_1 in subject_param_list if result_1>st_dev_start_1 and result_1<st_dev_end_1 ]
    st_dev_2_range=[result_2 for result_2 in subject_param_list if result_2>st_dev_start_2 and  result_2<st_dev_end_2]
    st_dev_3_range=[result_3 for result_3 in subject_param_list if result_3>st_dev_start_3 and  result_3<st_dev_end_3]

    #Adding objects with value in resemblence to standard deviation
    subject_param_graph=ff.create_distplot([subject_param_list],[str(choice_arg)],show_hist=False)
    subject_param_graph.add_trace(go.Scatter(x=[st_dev_start_1,st_dev_start_1],y=[0,0.17],mode="lines",name="Standard Deviation 1"))
    subject_param_graph.add_trace(go.Scatter(x=[st_dev_start_2,st_dev_start_2],y=[0,0.17],mode="lines",name="Standard Deviation 2"))
    subject_param_graph.add_trace(go.Scatter(x=[st_dev_start_3,st_dev_start_3],y=[0,0.17],mode="lines",name="Standard Deviation 3"))
    subject_param_graph.add_trace(go.Scatter(x=[st_dev_end_1,st_dev_end_1],y=[0,0.17],mode="lines",name="Standard Deviation 1"))
    subject_param_graph.add_trace(go.Scatter(x=[st_dev_end_2,st_dev_end_2],y=[0,0.17],mode="lines",name="Standard Deviation 2"))
    subject_param_graph.add_trace(go.Scatter(x=[st_dev_end_3,st_dev_end_3],y=[0,0.17],mode="lines",name="Standard Deviation 3"))

    #Updating the y-axis
    subject_param_graph.update_yaxes(range=[0,0.05])

    #Showing the graph and printing the statistics
    print("Generating graph...")
    time.sleep(2.3)
    subject_param_graph.show() 
    print("{}% of the students scored between {} and {} standard deviations.".format((len(st_dev_1_range)*100)/len(subject_df_list),round(st_dev_start_1,1),round(st_dev_end_1,1)))
    print("{}% of the students scored between {} and {} standard deviations.".format((len(st_dev_2_range)*100)/len(subject_df_list),round(st_dev_start_2,1),round(st_dev_end_2,1)))
    print("{}% of the students scored between {} and {} standard deviations.".format((len(st_dev_3_range)*100)/len(subject_df_list),round(st_dev_start_3,1),round(st_dev_end_3,1)))
    print("{} is the most common score".format(round(list_mode,1)))
    print("{} is the middle score".format(round(list_median,1)))

    #Printing the ending message
    print("Thank You for using PerformanceResult2021.py")  

  
#Reading data from the file using the library pandas
df=pd.read_csv("Performance.csv")

#Introductory text, displaying all primary options and integrating user input
print("Welcome to StudentPerformance.py. We provide data on a particular examination conducted, namely the performance of students and categorisation based on several parameters.")
subject_list=["Unusable_Element","Mathematics","Reading","Writing"]
subject_count=0
for subject in subject_list[1:]:
  subject_count+=1
  print(str(subject_count)+":"+subject)
user_input_1=str(input("Please enter  the index of the subject whose performance is to be evaluated."))
subject_choice=subject_list[int(user_input_1)]
subject_df=df[subject_choice]
subject_df_list=subject_df.tolist()

#Asking the user for further categorisation
#Case-1
if (VerifyCategorisation()=="Yes"):

  #Displaying all the scondary options and integrating corresponding inputs
  param_list=["Unusable_Element","Gender","Ethnicity","Lunch","Preparation"]
  param_count=0
  for param in param_list[1:]:
    param_count+=1
    print(str(param_count)+":"+param)
  user_input_2=str(input("Please enter the index of the parameter whose performance is to be evaluated."))    
  param_choice=param_list[int(user_input_2)]

  #Assessing all cases given by the user
  #Case-1
  if(user_input_2==1):
    gender_list=["Unusable_Element","Male","Female"]
    gender_count=0
    for gender in gender_list[1:]:
      gender_count+=1
      print(str(gender_count)+":"+gender)
    user_input_3=int(input("Please enter the index of the gender whose performance is to be evaluated."))   
    gender_choice=gender_list[user_input_3]
    ModifyDataframeAndGenerateGraph(gender_choice,"Gender")

  #Case-2  
  elif(user_input_2==2):
    ethnicity_list=["Unusable_Element","Group A","Group B","Group C","Group D"]
    ethnicity_count=0
    for ethnicity in ethnicity_list[1:]:
      ethnicity_count+=1
      print(str(ethnicity_count)+":"+ethnicity)
    user_input_4=int(input("Please enter the index of the ethnicity whose performance is to be evaluated."))   
    ethnicity_choice=ethnicity_list[user_input_4]
    ModifyDataframeAndGenerateGraph(ethnicity_choice,"Ethnicity")

  #Case-3
  elif(user_input_2==3): 
    lunch_list=["Unusable_Element","standard","free/reduced"]
    lunch_count=0
    for lunch in lunch_list[1:]:
      lunch_count+=1
      print(str(lunch_count)+":"+lunch)
    user_input_5=int(input("Please enter the index of the lunch consumed whose performance is to be evaluated."))   
    lunch_choice=lunch_list[user_input_5]
    ModifyDataframeAndGenerateGraph(lunch_choice,"Lunch")

  #Case-4  
  elif(user_input_2==4):
    preparation_list=["Unusable_Element","completed","none"]
    preparation_count=0
    for preparation in preparation_list[1:]:
      preparation_count+=1
      print(str(preparation_count)+":"+preparation)
    user_input_6=int(input("Please enter the index of the preparation conducted whose performance is to be evaluated."))   
    preparation_choice=preparation_list[user_input_6]
    ModifyDataframeAndGenerateGraph(preparation_choice,"Preparation")

  #Case-5  
  else:
    print("Request Terminated.")
    print("Invalid Input.")
    print("Thank You for using PerformanceResult2021.py")  
    

#Case-2
else:
  #Creating the graph and finiding mode,median,mean and standarad deviation
  subject_graph=ff.create_distplot([subject_df_list],[str(subject_choice)],show_hist=False)
  graph_mean=statistics.mean(subject_df_list)
  graph_st_dev=statistics.stdev(subject_df_list)
  graph_mode=statistics.mode(subject_df_list)
  graph_median=statistics.median(subject_df_list)

  #Categorising the standard deviation
  st_dev_start_1,st_dev_end_1=graph_mean-(1*graph_st_dev),graph_mean+(1*graph_st_dev)
  st_dev_start_2,st_dev_end_2=graph_mean-(2*graph_st_dev),graph_mean+(2*graph_st_dev)
  st_dev_start_3,st_dev_end_3=graph_mean-(3*graph_st_dev),graph_mean+(3*graph_st_dev)

  #Categorising the data according to standard deviation
  st_dev_1_range=[result_1 for result_1 in subject_df_list if result_1>st_dev_start_1 and result_1<st_dev_end_1 ]
  st_dev_2_range=[result_2 for result_2 in subject_df_list if result_2>st_dev_start_2 and  result_2<st_dev_end_2]
  st_dev_3_range=[result_3 for result_3 in subject_df_list if result_3>st_dev_start_3 and  result_3<st_dev_end_3]

  #Adding objects with value in resemblence to standard deviation
  subject_graph.add_trace(go.Scatter(x=[st_dev_start_1,st_dev_start_1],y=[0,0.17],mode="lines",name="Standard Deviation 1"))
  subject_graph.add_trace(go.Scatter(x=[st_dev_start_2,st_dev_start_2],y=[0,0.17],mode="lines",name="Standard Deviation 2"))
  subject_graph.add_trace(go.Scatter(x=[st_dev_start_3,st_dev_start_3],y=[0,0.17],mode="lines",name="Standard Deviation 3"))
  subject_graph.add_trace(go.Scatter(x=[st_dev_end_1,st_dev_end_1],y=[0,0.17],mode="lines",name="Standard Deviation 1"))
  subject_graph.add_trace(go.Scatter(x=[st_dev_end_2,st_dev_end_2],y=[0,0.17],mode="lines",name="Standard Deviation 2"))
  subject_graph.add_trace(go.Scatter(x=[st_dev_end_3,st_dev_end_3],y=[0,0.17],mode="lines",name="Standard Deviation 3"))

  #Updating the y-axis
  subject_graph.update_yaxes(range=[0,0.05])

  #Showing the graph and printing the statistics
  print("Generating graph...")
  time.sleep(2.3)
  subject_graph.show()
  print("{}% of the students scored between {} and {} standard deviations.".format((len(st_dev_1_range)*100)/len(subject_df_list),round(st_dev_start_1,1),round(st_dev_end_1,1)))
  print("{}% of the students scored between {} and {} standard deviations.".format((len(st_dev_2_range)*100)/len(subject_df_list),round(st_dev_start_2,1),round(st_dev_end_2,1)))
  print("{}% of the students scored between {} and {} standard deviations.".format((len(st_dev_3_range)*100)/len(subject_df_list),round(st_dev_start_3,1),round(st_dev_end_3,1)))
  print("{} is the most common score".format(round(graph_mode,1)))
  print("{} is the middle score".format(round(graph_median,1)))

  #Printing the ending message
  print("Thank You for using PerformanceResult2021.py")

#--------------------------------------------------------------PerformanceResult.py--------------------------------------------------------------#
    


