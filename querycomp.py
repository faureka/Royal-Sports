import csv
import os.path
from datetime import datetime
class PartyDetails():
	"""docstring for PartyDetails"""
	
	def __init__(self,*args):
		self.detailparty = []
		self.flag = False
		self.datetoday = None


	def detailsparty(self,PartyName,searchby):
		if os.path.isfile("main\BillDetails.csv"):
			with open("main\BillDetails.csv","r") as fcsv:
				fhandle = csv.reader(fcsv,delimiter = ",")
				for row in fhandle:
					if row[searchby].lower() == PartyName.lower():
						self.flag = True
						self.detailparty.append(tuple(row))
			fcsv.close()
			if not self.flag:
				return 0
			else:	 		
				self.datetoday = datetime.now()
				print self.datetoday.strftime('%d-%m-%Y')
				with open("Reports\%s_%s.csv"%(self.datetoday.strftime('%d-%m-%Y'),PartyName),"w+") as ftemp:
					ftemp_h = csv.writer(ftemp,delimiter = ",")
					for val in self.detailparty:
						ftemp_h.writerow(val)
				ftemp.close()
				os.startfile("Reports\%s_%s.csv"%(self.datetoday.strftime('%d-%m-%Y'),PartyName))
				return 1

		elif not os.path.isfile("main\BillDetails.csv"):
			return 2

