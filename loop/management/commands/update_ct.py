
from loop.models import *
from django.core.management.base import BaseCommand, CommandError
import xlrd

class LoopCT():
	def update(self):
		xl_file = xlrd.open_workbook('/Users/sourabhsingh/Downloads/test.xlsx')
		d = xl_file.sheet_by_name('Sheet1')
		c=0
		for r in range(1,d.nrows):
			id = int(d.cell(r,0).value)
			quantity=d.cell(r,1).value
			rate = d.cell(r,2).value
			amount = d.cell(r,3).value
			ct = CombinedTransaction.objects.get(id=id)
			ct.quantity=quantity
			ct.price = rate
			ct.amount = amount
			ct.save()
			c=c+1
			print c

class Command(BaseCommand):
    help = '''This is to update wrong CTs '''

    def handle(self,*args,**options):
        print("LOOP CT")
        print(datetime.date.today())
        loop_cts = LoopCT()
        loop_cts.update()