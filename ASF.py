import numpy as np

def amplitudeSelectiveFiltering(rgbvalues, amax = 0.002, delta = 0.0001):
    rgbvalues = np.transpose(rgbvalues)
    L = rgbvalues.shape[1]
    
    C = (1/(np.mean(rgbvalues,1)))

    Clong = np.transpose(np.array([C,]*(L)))
    C = rgbvalues * Clong -1
        
    F = np.abs(np.fft.fft(C,n=L,axis=1)/L) #kleine error met Matlab.. 
       
    W = (delta / np.abs(F[0,:]))
    W[np.abs(F[0,:]<amax)] = 1
    W = W.reshape([1,L])
    test = np.tile(W,[3,1])
    Ff = np.multiply(F,(test))
        
    C = np.transpose(np.array([(np.mean(rgbvalues,1)),]*(L))) * np.abs(np.fft.ifft(Ff)+1)
 
return np.transpose(C)
