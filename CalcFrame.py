#
# calculator.py
#
# Copyright 2011 Vijeenrosh P.W <hsorhteeniv@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.



import wx
class Calculator(wx.Frame):
	finished=True
	oper1=0.00
	oper2=0.00
	oper="nill"
	isset=False
	def __init__(self,size):
		wx.Frame.__init__(self,None,-1," Vij Calc",(300,300),size)
		self.panel = wx.Panel(self,-1)
		buttons=["st"]
		self.labels=['st','1','2','3','4','5','6','7','8','9','0','.','=']
		positions = ["st", (10,60),(50,60),(90,60),(10,100),(50,100),(90,100),(10,140),(50,140),(90,140),(10,180)]
		self.expr = wx.TextCtrl(self.panel,-1,"0.00",(10,20),(200,30),wx.ALIGN_RIGHT)
		#button1 = wx.Button(self.panel,5,"1",(10,60),(30,30))
		#button2 = wx.Button(self.panel,-1,"2",(50,60),(30,30))
		#button = wx.Button(self.panel,-1,"3",(10,100),(30,30))
		
		for i in range(1,11):
			buttons.append( wx.Button(self.panel,int(self.labels[i]),str(self.labels[i]),positions[i],(30,30)))
			self.Bind(wx.EVT_BUTTON,self.OnClick,buttons[i])	
		ce = wx.Button(self.panel,16,"CE",(190,60),(30,30))	
		decimal = wx.Button(self.panel,10,".",(50,180),(30,30))
		equal = wx.Button(self.panel,11,"=",(90,180),(30,30))
		plus = wx.Button(self.panel,12,"+",(150,60),(30,30))
		minus = wx.Button(self.panel,13,"-",(150,100),(30,30))
		multi = wx.Button(self.panel,14,"*",(150,140),(30,30))
		divide = wx.Button(self.panel,15,"/",(150,180),(30,30))
		self.CreateStatusBar()
		self.SetStatusText(" Operation = "+self.oper)
		self.Bind(wx.EVT_BUTTON,self.OnPlus,plus)
		self.Bind(wx.EVT_BUTTON,self.OnEqual,equal)		
		self.Bind(wx.EVT_BUTTON,self.OnMinus,minus)
		self.Bind(wx.EVT_BUTTON,self.OnMulti,multi)	
		self.Bind(wx.EVT_BUTTON,self.OnDivide,divide)
		self.Bind(wx.EVT_BUTTON,self.OnCE,ce)
				


	def OnClick(self,event):
		if self.finished :
			self.expr.Clear()
			self.expr.AppendText(str(event.GetId()))
			self.finished=False
		else:
			self.expr.AppendText(str(event.GetId()))

	def OnPlus(self,event):
		if self.finished:
			pass
		else:
			self.oper1=float(self.expr.GetValue())
			self.isset=True
			self.expr.Clear()
			self.oper="+"
			self.SetStatusText(" Operation = " +self.oper)
	
	def OnMinus(self,event):
                if self.finished:
                        pass
                else:
                        self.oper1=float(self.expr.GetValue())
                        self.isset=True
                        self.expr.Clear()
                        self.oper="-"
                        self.SetStatusText(" Operation = " +self.oper)
	def OnMulti(self,event):
                if self.finished:
                        pass
                else:
                        self.oper1=float(self.expr.GetValue())
                        self.isset=True
                        self.expr.Clear()
                        self.oper="*"
                        self.SetStatusText(" Operation = " +self.oper)

	def OnDivide(self,event):
                if self.finished:
                        pass
                else:
                        self.oper1=float(self.expr.GetValue())
                        self.isset=True
                        self.expr.Clear()
                        self.oper="/"
                        self.SetStatusText(" Operation = " +self.oper)

	def OnEqual(self,event):
		if self.finished:
			pass
		elif not self.isset:
			pass
		else:
			if self.oper=="+":
				self.expr.SetValue( str( self.oper1 + float( self.expr.GetValue()) ) )
			elif self.oper=="-":
				self.expr.SetValue( str( self.oper1 - float( self.expr.GetValue()) ) )
			elif self.oper=="*":
				self.expr.SetValue( str( self.oper1 * float( self.expr.GetValue()) ) )
			elif self.oper=="/":
				self.expr.SetValue( str( self.oper1 / float( self.expr.GetValue()) ) ) #need modification 
			else:
				pass
			self.isset=False
			self.oper="nill"
			self.SetStatusText("Operation = " +self.oper)
			self.finished=True
	def OnCE(self,event):
		self.expr.SetValue("")

