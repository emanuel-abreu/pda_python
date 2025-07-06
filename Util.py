import os
#from Edge import *
#from Transition import *
#from State import *

class Util: #PDA = (Q, Σ, δ, {qi}, F)    
	@staticmethod
	def testAB(a: str, b: str): # return bool
		return a==b

	@staticmethod
	def checkout(b: bool, w: str): 
		if(b): print(f'reconheceu: {w}')
		else: print(f'Não reconheceu: {w}')

	@staticmethod
	def readFile(fileName: str): # return String throws IOException {
		f, res, dir = None, '', os.getcwd()+'\\'
		try:
			f = open(dir + fileName, "r")
			res = f.read()
		except FileNotFoundError:
			print(f'This file({fileName}) doesn\'t exist')
		finally:
			f.close()
		return res
	
	@staticmethod
	def writeFile(fileName: str, content: str): 
		f, dir = None, os.getcwd()+'\\'
		try:
			f = open(dir + fileName, 'w')
			f.write(content)
		except Exception as e:
			print(str(e))
		finally:
			f.close()
