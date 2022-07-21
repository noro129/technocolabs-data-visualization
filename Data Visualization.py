#Data Visualization
##Line Charts

#1
museum_data = pd.read_csv(museum_filepath,index_col="Date",parse_dates=True)

#2
museum_data.tail()

ca_museum_jul18 = 2620
avila_oct18 =19280-4622

#3
sns.lineplot(data=museum_data)

#4
#A
sns.lineplot(data=museum_data["Avila Adobe"],label="Avila Adobe")

##Bar Charts and Heatmaps

#1
ign_data = pd.read_csv(ign_filepath,index_col="Platform")

#2
ign_data

high_score = ign_data.max(axis=1)["PC"]
worst_genre = 'Simulation'

#3
#A
plt.figure(figsize=(14,14))

sns.barplot(y=ign_data.index,x=ign_data["Racing"])

#4
#A
plt.figure(figsize=(10,10))

sns.heatmap(data=ign_data,annot=True)

##Scatter Plots

#1
candy_data = pd.read_csv(candy_filepath,index_col="id")

#2
candy_data.head()

more_popular = '3 Musketeers'
more_sugar = 'Air Heads'

#3
#A
sns.scatterplot(x=candy_data["sugarpercent"],y=candy_data["winpercent"])

#4
#A
sns.regplot(x=candy_data["sugarpercent"],y=candy_data["winpercent"])

#5
sns.scatterplot(x=candy_data["sugarpercent"],y=candy_data["winpercent"],hue=candy_data["chocolate"])

#6
#A
sns.lmplot(x="sugarpercent",y="winpercent",hue="chocolate",data=candy_data)

#7
#A
sns.swarmplot(x=candy_data["chocolate"],y=candy_data["winpercent"])

##Distributions

#1
cancer_data = pd.read_csv(cancer_filepath,index_col='Id')

#2
cancer_data.head()

max_perim = 87.46

mean_radius = 9.504

#3
#A
sns.histplot(data=cancer_data,x='Area (mean)',hue="Diagnosis")

#4
#A
sns.kdeplot(x='Radius (worst)',hue='Diagnosis',data=cancer_data)
