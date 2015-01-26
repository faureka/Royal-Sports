from Tkinter import *
import ttk
import tkMessageBox as tkmb
from csv import *
from dateinput import *
from csvmodule import *
from ACCombo import *
from ACEntry import *
from ComplistAC import *
from querycomp import *
states = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh'
,'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
'Odisha(Orissa)','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

fields = ["Party Name","Bill No.","Amount","Date(dd/mm/yyyy)","TIN No.","State","Debit/Credit"]



class BillDetails(Frame):
	"""docstring for BillDetails"""
	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.poplist()
		self.createwidget()
		self.grid()
		self.inpdata = []	
		self.ACcomplist = []
		self.querycompany = None

	def poplist(self):
		complist = CsvReader()
		self.ACcomplist = complist.csvreader(0)	

	def SubmitData(self):
		self.inpdata = []
		self.inpdata.append(self.entry1.get())
		self.inpdata.append(self.entry2.get())
		self.inpdata.append(self.entry3.get())
		self.inpdata.append(self.entry4.get())
		self.inpdata.append(self.entry5.get())
		self.inpdata.append(self.entry6.get())
		self.inpdata.append(self.entry7.get())
		self.WriteCsv(self.inpdata) 
	
	def WriteCsv(self,*args):
		for i in xrange(len(self.inpdata)):
			if self.inpdata[i] == '':
				tkmb.showinfo("Warning","One or More Fields are Empty!")
				return
				break
			# print self.inpdata[i]
		writer = csvwriter()
		writer.csvwrite(self.inpdata)

	def GenerateData(self):
		self.querycompany = self.entry8.get()
		queryobj = PartyDetails()
		self.retval = queryobj.detailsparty(self.querycompany)
		if self.retval == 0:
			tkmb.showinfo("Warning","Party Doesn't exists! Please Recheck.")
		elif self.retval ==2:
			tkmb.showinfo("Warning","File Missing!")
		else:
			return	
			

	def ClearData(self):
		self.entry1.delete(0,END)	
		self.entry2.delete(0,END)	
		self.entry3.delete(0,END)	
		self.entry5.delete(0,END)	
		self.entry6.delete(0,END)	
		self.entry4._delete(0,END)	

	def createwidget(self):
		'''variables Intializations'''
		self.var = StringVar(root)
		self.state = StringVar(root)
		
		self.label1 = Label(root,text = "Party Name")
		self.label2 = Label(root,text = "Bill No.")
		self.label3 = Label(root,text = "Amount")
		self.label4 = Label(root,text = "Date(dd/mm/yyyy)")
		self.label5 = Label(root,text = "TIN No.")
		self.label6 = Label(root,text = "State")
		self.label7 = Label(root,text = "Debit/Credit")
		self.label8 = Label(root,text = "Query a Company")
		# self.entry1 = Entry(root)
		self.entry1 = AutocompleteCombobox(root)
		self.entry1.set_completion_list(self.ACcomplist)
		self.entry1.focus_set()

		self.entry2 = Entry(root)
		self.entry3 = Entry(root)
		self.entry4 = DateEntry(root)	
		self.entry5 = Entry(root)
		# self.entry6 = ttk.Combobox(root,textvariable = self.state)
		
		self.entry6 = AutocompleteCombobox(root)
		self.entry6.set_completion_list(states)
		# self.entry6.focus_set()
		# self.entry7 = ttk.Combobox(root,textvariable = self.var)
		# self.entry7['values'] = ("Dr.","Cr.")
		
		self.entry7 = AutocompleteCombobox(root)
		self.entry7.set_completion_list(['Dr','Cr'])
		# self.entry7.focus_set()
		# self.entry7.current(0)

		self.entry8 = AutocompleteCombobox(root)
		self.entry8.set_completion_list(self.ACcomplist)
		self.entry8.focus_set()

		self.submit = Button(root,text = "Submit", command = self.SubmitData,font=("Helvetica", "12"),bg = "#5CBD7D")
		self.clear 	= Button(root,text = "Clear", command = self.ClearData,font=("Helvetica", "12"),bg = "#E60000")
		self.query  = Button(root,text = "Generate Report", command = self.GenerateData,font=("Helvetica", "12"),bg = "#3059AC")

		self.label1.grid(sticky=W,padx = 5,pady = 5)
		self.label2.grid(sticky=W,padx = 5,pady = 5)
		self.label3.grid(sticky=W,padx = 5,pady = 5)
		self.label4.grid(sticky=W,padx = 5,pady = 5)
		self.label5.grid(sticky=W,padx = 5,pady = 5)
		self.label6.grid(sticky=W,padx = 5,pady = 5)
		self.label7.grid(sticky=W,padx = 5,pady = 5)
		self.label8.grid(padx = 5,pady = 5,column = 4,row = 0)

		self.entry1.grid(row=0, column=1,padx = 5,pady = 5)
		self.entry2.grid(row=1, column=1,padx = 5,pady = 5)
		self.entry3.grid(row=2, column=1,padx = 5,pady = 5)
		self.entry4.grid(row=3, column=1,padx = 5,pady = 5)
		self.entry5.grid(row=4, column=1,padx = 5,pady = 5)
		self.entry6.grid(row=5, column=1,padx = 5,pady = 5)
		self.entry7.grid(row=6, column=1,padx = 5,pady = 5)
		self.entry8.grid(row=1, column=4,columnspan = 2,padx = 5,pady = 5)

		self.submit.grid(row=7, columnspan = 2,sticky = N+E+W+S,pady = 5 ,padx = 5)
		self.clear.grid(row = 8, columnspan = 2,sticky = N+E+W+S,pady = 5 ,padx = 5)
		self.query.grid(row =2,column = 4,columnspan = 2,sticky = N+E+W+S,pady = 5 ,padx = 5 )

root = Tk()
root.title("Bill Master")
app = BillDetails(master = root)
app.mainloop()
