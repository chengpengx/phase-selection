import obspy
import matplotlib.pyplot as plt
from dela_data import data_writer
import os
import numpy as np
def nom_stream(stream):
	stream = stream/max(stream)
	return stream
def preprocess(stream):
	pass	
def cut_event(stream,T1):
	a = stream[T1-200:T1+200]
	return a	
def cut_noise(stream):
	a = stream[0+2000:0+2400]
	return a
def convert(stream,output_path,lable):    
	writer = data_writer(output_path)
	writer.write(stream,lable)
	writer.close()
def mix(a,b,w1,w2):
	return w1*a+w2*b
def main():
	for root,dirs,files in os.walk('snr_h5'):
		a = len(files)
		record = [0]*a
		i = 0
		for file in files:
			record[i] = obspy.read('snr_h5/'+file,format='SAC')
			record[i] = record[i].normalize()
			r = record[i][0]
			T1 = int(200*r.stats.sac.t1)
			r = r.data
			#plt.plot(r)
			#plt.show()
			c = []
			b = np.random.normal(0,0,len(r))
			c = r+b
			#c = nom_stream(c)
			#plt.plot(r)
			#plt.plot(c)
			#plt.show()
			#exit()
			#print(np.mean(a[0].data),np.std(a[0].data))
			w = cut_noise(c)
			#plt.xticks(range(0,3),color="k",fontsize=10)
			#plt.xlabel("Time/s",fontsize=15)
			#plt.ylabel("Amplitude",fontsize=15)
			plt.plot(np.arange(0,2,0.005),w,color="k")
			#plt.scatter(1,0,marker="x",color="r",s=200,alpha=1)
			plt.show()
			exit()
			if len(w)==400:
				output_name = file.split(".pick")[0] +"0.1"+".tfrecords"
				output_path = os.path.join('rrsac/event', output_name)
				convert(w,output_path,1)
				print(i)
				i+=1
			else:
				continue
			'''j = 0
			writer = data_writer(output_path)
			for j in range(len(c)-400):
				writer.write(c[j:j+401],0)
				j+=1
			print(j)'''
if __name__ =='__main__':
    main() 

