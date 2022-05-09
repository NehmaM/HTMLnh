import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["College"]
print("database connected!")

mycol = mydb["studlist"]
print("collection created!")


#--------------------------------------
#Check if database exists:
dblist = myclient.database_names()
if "College" in dblist:
  print("The database exists.")

#---------------------------------------
#Check if the collection exists:
collist = mydb.collection_names()
print(collist)
if "studlist" in collist:
  print("The collection exists.")
else:
  print("The collection doesnt exists.")


print(mydb.studlist.find({"course":"MCA"}).count())
for i in mydb.studlist.find({"course":"MCA"}):
	print()










'''
result = mydb.mycol.find( { "$where": function() { return("this.course == MCA")}})
for compare_fields in result:
    print(compare_fields)


#>mydb.mycol.find( { "$where": function() { return (this.course == this.science) }}).pretty();

#comp_keys = ['course', 'gender']
#for i in studlist:
#	comp_keys[0] = ''
			



if 'course'='MCA' and  'gender'="female":
	print(name)
	print(mark)

'''	




	 
