#EXERCICE1:
    
import pandas as pd
df = pd.read_csv(r"C:\Users\hp\OneDrive\Bureau\Automobile_data.csv")
print(df.head(5))
print(df.tail(5))

#EXERCICE2:
    
nan_values = df.isna().any()
print (nan_values)
df['price'] = df['price'].fillna(0)

#EXERCICE3:
    
a = df [['company','price']][df.price==df['price'].max()]
print(a)

#EXERCICE4:
     
Toyodf = df.groupby(by='company')
print(Toyodf.get_group("toyota"))

#EXERCICE5:
    
count = df['company'].value_counts()
print(count)

#EXERCICE6:
    
cars = df.groupby('company')
highprice = cars['price'].max()
print(highprice)

#EXERCICE7:

cars = df.groupby('company')   
mean = cars['company','average-mileage'].mean()
print(mean)

#EXERCICE8:
    
cars = df.sort_values(by=['price', 'horsepower'], ascending=False)
print(cars.head(5))

#EXERCICE9:

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
Df1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
Df2 = pd.DataFrame.from_dict(japaneseCars)

df = pd.concat([Df1,Df2], keys=["Germany", "Japan"])
print(df)

#EXERCICE10:

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
df1 = pd.DataFrame.from_dict(Car_Price)
horsepower = [141,80,182,160]
df1['horsepower']=horsepower
print(df1)

