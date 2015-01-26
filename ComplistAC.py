from csv import *
import os.path

class CsvReader:
	"""docstring for CsvReader"""
	def __init__(self, *args):
		self.complist = []


	def csvreader(self,rowno):
		if os.path.isfile("main\BillDetails.csv"):
			with open("main\BillDetails.csv","r") as fcsv:
				fhandle = reader(fcsv,delimiter = ",")
				for row in fhandle:
					self.complist.append(row[rowno])
			fcsv.close()
			return self.complist	
		else:
			with open("main\BillDetails.csv","a+") as fcsv:
				fhandle = reader(fcsv,delimiter = ",")
				for row in fhandle:
					self.complist.append(row[rowno])
			fcsv.close()
			return self.complist	

if __name__ == '__main__':
	fd = CsvReader()
	print fd.csvreader(2)
