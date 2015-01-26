from csv import *


class csvwriter:
	"""docstring for csvwriter"""
	def __init__(self,*args):
		return

	def csvwrite(self,bdetals):
		with open("main\BillDetails.csv","a+") as fcsv:
			fhandle = writer(fcsv,delimiter =",",quotechar = "|",
							quoting=QUOTE_MINIMAL)
			fhandle.writerow(bdetals)
			fcsv.close()

				
if __name__ == '__main__':
	bdetals = ["faizan","Abbas","1234.00","12329AA","12/24/2014","Dr."]
	fd = csvwriter()
	fd.csvwrite(bdetals)