import subprocess 
from mpi4py import MPI

world_comm = MPI.COMM_WORLD
world_size = world_comm.Get_size()
my_rank = world_comm.Get_rank()



class Likelihood: 
	def __init__(self,data_):
		global my_rank
		self.data = data_
		self.ruta = 'data' + str(my_rank) + '.dat'
		self.rutaG = './main data'+ str(my_rank) + '.dat >temporal' + str(my_rank) + '.dat'
		self.calc()
		self.omega = self.calc_omega()
		self.mchi2 = self.find_mx2()
		self.like_omega = self.l_omega()
		self.log_like = self.gaussian()
		self.diccionario2 = {'Mchi2':self.mchi2, 'Densidad reliquia':self.omega,'loglikelihood':self.log_like}
		self.data.update(self.diccionario2)

	def writer(self,file,dictionary):
		data1=open(file,'w')
		for items in dictionary.items(): 
			data1.write("%s %s\n"%items)
		data1.close()

	def calc(self): 
	    self.writer(self.ruta,self.data) 
	    subprocess.getoutput(self.rutaG)

	'''
	def ejecutar(self):
		self.calc()
		self.omega=self.calc_omega()
		self.mchi2 = self.find_mx2()
		self.like_omega = self.l_omega()
		self.log_like = self.gaussian()
		self.diccionario2 = {'Mchi2':self.mchi2, 'Densidad reliquia':self.omega,'loglikelihood':self.log_like}
		self.data.update(self.diccionario2)
	'''
	
	def find_command(self,COMMAND):
		const = 0.0 
		dato = subprocess.getoutput(COMMAND)
		if(len(dato)>0):
			const = float(dato)
		elif np.isnan(dato):
			const = -1 
		else: 
			const = -1 
		return const
	
	'''
	def find_command(self, COMMAND):
	    const = 0.0 
	    dato = subprocess.getoutput(COMMAND).strip()  # Elimina espacios en blanco al principio y al final
	    if dato.replace(".", "").replace("e", "").replace("-", "").replace("+", "").isdigit():
	        const = float(dato)
	    else: 
	        const = -1 
	    return const
	'''
	
	def find_mx2(self):
	    COMMAND_MCHI2 = "grep 'Mchi1' temporal" + str(my_rank) + ".dat | awk 'BEGIN{FS=\" \"};{print $11}' "
	    return self.find_command(COMMAND_MCHI2)

	def calc_omega(self):
		COMMAND_RQ = "grep 'Omega' temporal" + str(my_rank) + ".dat | awk 'BEGIN{FS=\"=\"};{print $3}'"
		return self.find_command(COMMAND_RQ)

	def l_omega(self):
		omega_th = self.omega
		omega_ex = 0.12
		delta_omega_pdg = ((0.05*omega_th)**2 + 0.001*2)**0.5
		return (omega_th - omega_ex)**2 / delta_omega_pdg**2

	def gaussian(self): 
		return self.l_omega()

	def __str__(self):
		texto=f'Los resultados son'
		for clave, valor in self.data.items():
			texto += '\n'
			texto+=f"{clave} = {valor}"
		return texto

	def get_gaussian(self):
		return self.log_like

	def get_datos(self):
		return self.data 

if __name__ == '__main__':
	
	import random

	valorMasaChi = random.randint(-3,1)
	valorMasaA = random.randint(-3,1)
	valorMasaH = random.randint(-3,1)
	x = [valorMasaA,valorMasaH,valorMasaChi,-1,-4,-2]

	def diccionario(x_):
		data = {'MAp':3., 'mphi':1,'Mchi1':0.1,'angle':1e-3,'gX':0.1182,'epsilon':0.1,'ff':0.10}
		data['MAp'] = 10**x_[0] #Logaritmico
		data['mphi'] = 10**x_[1] #Logaritmico
		data['Mchi1'] = 10**x_[2] #Logaritmico
		#data['Mchi1'] = x_[2] #Lineal
		data['gX'] = 10**x_[3] #Logaritmico
		data['epsilon'] = 10**x_[4] #Logaritmico
		data['ff'] = 10**x_[5] #lineal
		return data

	ob1 = Likelihood(diccionario(x))
	ob1.get_datos()
	print(ob1)

	#print(ob1)
	#obj = [] 
	#obj.append(ob1.get_datos())
	#print(obj)
	#print(pd.DataFrame(obj))
	#print(ob1.get_gaussian())