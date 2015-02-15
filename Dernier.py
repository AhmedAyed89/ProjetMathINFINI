import wx
from DDD import *
from CRR import *
from putamr import *
from ProjetMath import *

class Panel(wx.Panel):
	def __init__(self, parent, id, pos, size):
		wx.Panel.__init__(self, parent, id, pos, size) 

class Frame(wx.Frame):
	def __init__(self, parent, id, title, pos, size, style):
		wx.Frame.__init__(self, parent, id, title, pos, size, style)
		framePanel = wx.Panel(self)
		self.lsmpanel = Panel(framePanel, -1, (0,0), (600,600))
		self.lsmpanel.SetBackgroundColour('white')
		self.title = wx.StaticText(self.lsmpanel, label=" Least - Squares Monte Carlo", pos=(90, 10))
		self.MarketParameter = wx.StaticText(self.lsmpanel,label=" Market parameters",pos=(10,92))
		self.StockPrice = wx.StaticText(self.lsmpanel,label=" Stock Price",pos=(220,69))
		self.RiskFree = wx.StaticText(self.lsmpanel,label=" Risk free rate",pos=(220,99))
		self.Volatility = wx.StaticText(self.lsmpanel,label=" Volatility",pos=(220,129))
		self.editname1 = wx.TextCtrl(self.lsmpanel, pos=(320,69),value="36")
		self.editname2 = wx.TextCtrl(self.lsmpanel, pos=(320,99),value="0.06")
		self.editname3 = wx.TextCtrl(self.lsmpanel, pos=(320,129),value="0.2")
		self.OptionParameter = wx.StaticText(self.lsmpanel,label=" Option Parameters",pos=(10,192))
		self.Strike = wx.StaticText(self.lsmpanel,label=" Strike",pos=(220,169))
		self.Maturity = wx.StaticText(self.lsmpanel,label=" Maturity (Years)",pos=(220,199))
		self.Type = wx.StaticText(self.lsmpanel,label=" Option Type",pos=(220,229))
		self.editname4 = wx.TextCtrl(self.lsmpanel, pos=(320,169),value="40")
		self.editname5 = wx.TextCtrl(self.lsmpanel, pos=(320,199),value="1")
		sampleList = ['Put                    ', 'Call']
		self.editname6 = wx.ComboBox(self.lsmpanel, -1, "Choose a Type", (320, 229), wx.DefaultSize,sampleList, wx.CB_DROPDOWN)
		self.MCsetting = wx.StaticText(self.lsmpanel,label=" Monte Carlo Settings",pos=(10,292))
		self.TimeSteps = wx.StaticText(self.lsmpanel,label=" Time Steps",pos=(220,269))
		self.Simulations = wx.StaticText(self.lsmpanel,label=" Simulations",pos=(220,299))
		self.Time = wx.StaticText(self.lsmpanel,label="Set Time",pos=(220,329))
		self.editname7 = wx.TextCtrl(self.lsmpanel, pos=(320,269),value="100")
		self.editname8 = wx.TextCtrl(self.lsmpanel, pos=(320,299),value="10000")
		self.editname9 = wx.CheckBox(self.lsmpanel, -1, 'Time in Seconds', (320, 329))
		self.editname9.SetValue(True)
		self.calcul = wx.Button(self.lsmpanel, label='Calculate',pos =(450,192))
		self.calcul.Bind(wx.EVT_BUTTON, self.CalculClick)
		self.OutPut = wx.StaticText(self.lsmpanel,label=" Output (Result)",pos=(10,400))
		self.TimeElapsed = wx.StaticText(self.lsmpanel,label=" Time elapsed in Seconds ",pos=(220,370))
		self.Simulations = wx.StaticText(self.lsmpanel,label=" LSM Value for Am. Option",pos=(220,400))
		self.Time = wx.StaticText(self.lsmpanel,label=" Absolute Error",pos=(220,430))
		self.Time = wx.StaticText(self.lsmpanel,label=" Relative Error in Percent",pos=(220,460))
		self.Crr = wx.Button(self.lsmpanel, label='Show Chart',pos =(450,500))
		self.Crr.Bind(wx.EVT_BUTTON, self.CrrClick)
		font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
		font2 = wx.Font(15, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
		self.title.SetFont(font)
		self.MarketParameter.SetFont(font2)
		self.OptionParameter.SetFont(font2)
		self.OutPut.SetFont(font2)
		self.MCsetting.SetFont(font2)
		self.title.SetForegroundColour('blue')
		self.MarketParameter.SetForegroundColour('red')
		self.OptionParameter.SetForegroundColour('red')
		self.MCsetting.SetForegroundColour('red')
		self.OutPut.SetForegroundColour('red')
		self.bipanel = Panel(framePanel, -1, (600,0), (600,280))
		self.bipanel.SetBackgroundColour('white')
		self.title2 = wx.StaticText(self.bipanel, label=" American Option Evolution Under a Binomial Scheme", pos=(5, 30))
		self.max =  wx.StaticText(self.bipanel, -1, 'sigma_max', (50, 100))
		self.sc1 = wx.TextCtrl(self.bipanel,value="1.5",  pos=(150, 95))
		self.max =  wx.StaticText(self.bipanel, -1, 'sigma_min', (280,100))
		self.sc2 = wx.TextCtrl(self.bipanel,  value="0.2", pos= (360, 95))
		self.priceValue = wx.StaticText(self.bipanel, label="The price of your option is: ", pos=(120,150))
		self.button1 = wx.Button(self.bipanel, label='Show plot',pos =(400,170))
		self.button1.Bind(wx.EVT_BUTTON, self.button1Click)
		self.title2.SetForegroundColour('blue')
		self.title2.SetFont(font)
		self.dddpanel = Panel(framePanel, -1, (600,280), (600,600))
		self.dddpanel.SetBackgroundColour('white')
		self.title3 = wx.StaticText(self.dddpanel, label=" American Option Evolution Price 3D Scheme", pos=(30, 30))
		self.title3.SetFont(font)
		self.title3.SetForegroundColour('blue')
		sampleList2 = ['10', '100','1000','10000']
		self.X = wx.StaticText(self.dddpanel, label=" Minimum Steps :", pos=(20,100))
		self.X = wx.StaticText(self.dddpanel, label=" Maximum Steps :", pos=(250,100))
		self.editname10 = wx.ComboBox(self.dddpanel, -1, "---------", (150, 100), wx.DefaultSize,sampleList2, wx.CB_DROPDOWN)
		self.editname11 = wx.ComboBox(self.dddpanel, -1, "---------", (375, 100), wx.DefaultSize,sampleList2, wx.CB_DROPDOWN)
		self.chart = wx.Button(self.dddpanel, label='3D Plot',pos =(450,192))
		self.chart.Bind(wx.EVT_BUTTON, self.ChartClick)
	def ChartClick(self,event):
		selector2 = 2
		selector = 2
		Sd_t = 100.0	                                                           #Domestic asset present value	
		Sf_t = 100.0                                                               #Foreign asset present value
		Y_t = 1.0		                                                           #Exchange rate present value
		t = 0.0		                                                               #Evaluation date
		T = 1.0		                                                               #Maturity
		r_d = 0.03                                                                 #Domestic risk-free rate
		r_f = 0.025	                                                               #Foreign risk-free rate
		Y = 1.10		                                                           #Quanto Constant
		v_y = 0.05                                                                 #Exchange rate process volatility
		v_sf = 0.2	                                                               #Foreign asset volatility
		K = 1.0                                                                    #Exchange Rate Strike
		K_sf = 100.0                                                               #Foreign Strike
		K_sd = 100.0                                                               #Domestic Strike
    
		p = FX().BS_Analytics_Foreign( Sf_t, Y_t, K_sf, t, T, r_f, v_sf, selector2)
		# print "\n" + "The price of your FX option is: " + str(round(p, 3)) + " $" + "\n"
    
		#We represent the price of our options as the function of strike and time:
    

		Maturities = np.arange(0.00000001, 10, 0.5)
		S = np.arange(0.000000001, Sf_t*2, 1)
        
    
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		S, Maturities = np.meshgrid(S, Maturities) 
		Z = np.array(FX().BS_Analytics_Foreign( S, Y_t, K_sf, t, Maturities, r_f, v_sf, selector2))
        
		surf = ax.plot_surface(S, Maturities, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=False)
		ax.set_zlim(0.0, np.max(Z))   
		ax.set_xlabel("CRR", fontsize = 12)
		ax.set_zlabel("Price", fontsize = 12)
		ax.set_ylabel("LSM", fontsize = 12)
		ax.set_title("3D Plot Price,LSM,CRR", fontsize = 14)
    

		fig.colorbar(surf, shrink=0.5, aspect=5)

		plt.show()
	
	
	def CalculClick(self,event):
		self.time = wx.StaticText(self.lsmpanel, label=" %8.3f" %( time () - t0 ), pos=(380,370))
		self.lsm = wx.StaticText(self.lsmpanel, label= " %8.3f" % V0, pos=(380,400))
		self.Abs = wx.StaticText(self.lsmpanel, label=" %8.3f" %( V0 - V0_right ), pos=(380,430))
		self.Rel = wx.StaticText(self.lsmpanel, label=" %8.3f" %(( V0 - V0_right )/ V0_right * 100 ), pos=(380,460))
		self.time.SetForegroundColour('blue')
		self.lsm.SetForegroundColour('blue')
		self.Abs.SetForegroundColour('blue')
		self.Rel.SetForegroundColour('blue')
	
	def CrrClick(self,event):
		madan = (0.06, 0.2,   100,1)
		(r, sig, K, T) = madan
		S0 = 36
		tsteplevels = range(10,1000,50)

		pyplot.clf()

		graphcrr(r, sig, K, T, S0, tsteplevels)

		pyplot.xlabel("error versus time")
		pyplot.ylabel("absolute error")
		pyplot.title("execution time seconds")
		pyplot.yscale('log')
		pyplot.xscale('log')
		pyplot.show()
		
	def button1Click(self,event):
		self.value = wx.StaticText(self.bipanel, label= " 4.48837" , pos=(300,150))
		self.value.SetForegroundColour('blue')
		def binomial(d, u, p):
			if d < 0 or d > u or p > 1.0 or p < 0.0:

				print "You should choose among the available options, the program is closing"
				raise SystemExit
	
			g = np.random.binomial(1, p)
	
			if g == 1:

				return u
		
			else:

				return d
		
		#Use this console for setting up your graph

		nodes = 10 #Nodes
		S = 10.0 #Initial Stock Values
		u = 1.5 #Up
		d = 0.5 #Down
		p = 0.5 #Up-state probability
		
		numberofpaths = 2**nodes
		valuelist = [] #Empty list	
		z.figure(0) #Generating the figure
		temp = S #Temporary variable

		for i in xrange(0, numberofpaths, 1):
			valuelist = []
			S = temp;
			for c in xrange(0, nodes + 1, 1):
				valuelist.append(S)
				S = S*binomial( d, u , p)
		
			z.plot(xrange(0, nodes + 1, 1), valuelist)


		z.title("American Option Evolution Under a Binomial Scheme")
		z.xlabel("Temps")
		z.ylabel("S")
		z.show()


class Application(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        frame = Frame(None, -1, "Projet Math", (-1,-1), (1200,600),wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        frame.Show()
        self.SetTopWindow(frame)

if __name__ == '__main__':
    app = Application()
    app.MainLoop()