#Case Study on mtcars dataset in Python	download data

#Download data
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data
mtcars
# Dataframe
# Dataset of 23 cars in rows with 11 columns indicating 11 different variables (specifications) that are varied across cars
# Columns are mpg,cyl,disp,hp,drat,wt,qsec,vs,am,gear and carb. Each has a differnet set of levels (or values) they can take.
mtcars.columns()

#print first / last few rows
print(mtcars.head())
print(mtcars.tail())
#print number of rows and columns
rows, columns = mtcars.shape
print(rows)
print(columns)
#print names of columns
for col in mtcars:
    print(col)
    
#Filter Rows
print(mtcars[(mtcars["gear"]==5) & (mtcars["cyl"]==8)])

#cars with cyl=8
print(mtcars[(mtcars["cyl"]==8)])

#cars with mpg <= 27
print(mtcars[(mtcars["mpg"]<=27)])

#rows match auto tx

#First Row
print(mtcars.head(1))

#last Row
print(mtcars.tail(1))

# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(mtcars.iloc[[1,4,7,25],[1,6,7]])

# first 5 rows and 5th, 6th, 7th columns of data frame
print(mtcars.iloc[:5,[5,6,7]])

#rows between 25 and 3rd last
print(mtcars.iloc[25:-3])

#alternative rows and alternative column
print(mtcars.iloc[::2,::2])

#find row with Mazda RX4 Wag and columns cyl, am
print(mtcars.loc["Mazda RX4 Wag",['cyl','am']])

#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am
print(mtcars.loc["Merc 280":"Volvo 142E",['cyl','am']])

# mpg > 23 or wt < 2
print(mtcars[(mtcars["mpg"]>23) & (mtcars["wt"]<2)])

#using lambda for above
filter_cond = lambda x: (x['mpg'] > 23) & (x['wt'] < 2)
print(mtcars[mtcars.apply(filter_cond, axis=1)])

#with or condition
print(mtcars[(mtcars["mpg"]>23) | (mtcars["wt"]<2)])

#find unique rows of cyl, am, gear
print(mtcars[['cyl','am','gear']].drop_duplicates())

#create new columns: first make a copy of mtcars to mtcars2
mtcars2 = mtcars.copy()
mtcars2["NewCol"] = 1
print(mtcars)
#keeps other cols and divide displacement by 61
print(mtcars2["disp"]/61)

# multiple mpg * 1.5 and save as original column
mtcars2["mpg"] = mtcars2["mpg"]*1.5
print(mtcars2)
