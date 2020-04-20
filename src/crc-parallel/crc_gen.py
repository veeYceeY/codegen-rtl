
import numpy as np


class crcgen:
	def __init__(self,poly,input_size,poly_size):
		self.poly = poly
		self.input_size = input_size
		self.poly_size = poly_size
	def calc_matrix(self):
		#print (self.input_size)
		#print (self.poly_size)
		x=np.zeros((self.poly_size,self.input_size),np.int32)
		y=np.zeros((self.poly_size,self.input_size),np.int32)
		z=np.zeros((self.poly_size,self.input_size),np.int32)
		
		for j in range(self.poly_size):
			for i in range(self.input_size):
				#print(j,i)
				if i==0:
					x[j,i]=self.poly[j]
				elif i==j+1:
					x[j,i]=1
				else:
					x[j,i]=0
		np.savetxt('part.txt',x,fmt='%d')
		power=0
		y=x;
		for power in range(self.poly_size-1):
			z=np.zeros((self.poly_size,self.input_size),np.int32)
			for j in range(self.poly_size):
				for i in range(self.input_size):
					for k in range(self.input_size):
						t=x[i,k]*y[k,j]
						
						if z[i,j]==t:
							z[i,j]=0
						else:
							z[i,j]=1
						#print(power,j,i,x[j,i],x[i,j],y[j,i])
			y=z;
			#print(y)
		return y

	def gen_code(self):
		f=open("crc32.vhd","w");
		f.write("entity crc32 is \n\tport(\n\t\ti_data : std_logic_vector(31 downto 0);\n\t\to_crc  : std_logic_vector(31 downto 0)\n\t);\nend entity;\n\narchitecture behavioral of crc32 is\n\tsignal d: std_logic_vector(31 downto 0);\n\tsignal c: std_logic_vector(31 downto 0);\nbegin\n\n  d<= i_data;\n  o_crc<= c;\n")

		c=self.calc_matrix()
		for j in range(self.poly_size):
			f.write("  c(")
			f.write(str(31-j))
			f.write(")=")
			for i in range(self.input_size):
				if c[j,i] == 1:
					f.write("d(")
					f.write(str(31-i))
					f.write(")+")
					f.write("c(")
					f.write(str(31-i))
					f.write(")")
					if i < 31 :
						f.write("+")
			f.write(";\n")
		f.write("\n\nend architecture ;")
		return c
			





crc= crcgen([0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1],32,32);
#crc= crcgen([1,0,0,1],4,4);
#mat=crc.calc_matrix();
mat=crc.gen_code();
np.savetxt('coeff.txt',mat,fmt='%d')
#print(mat);
