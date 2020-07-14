import numpy as np
np.random.seed(1)
def relu(x):
    return (x > 0) * x
def relu2deriv(output):
    return output>0
streetlights = np.array( [[ 1, 0, 1 ],
                          [ 0, 1, 1 ],
                          [ 0, 0, 1 ],
                          [ 1, 1, 1 ] ] )
walk_vs_stop = np.array([[ 1, 1, 0, 0]]).T
alpha = 0.2
hidden_size = 4
weights_0_1 = 2*np.random.random((hidden_size,3)) - 1  # (4,3)
weights_1_2 = 2*np.random.random((1,hidden_size)) - 1  # (1,4)
for iteration in range(60):
    layer_2_error = 0
    for i in range(len(streetlights)):
        layer_0 = streetlights[i:i+1].T             # (3,1)
        layer_1 = relu(np.dot(weights_0_1,layer_0)) # (4,1)
        layer_2 = np.dot(weights_1_2,layer_1)       # 1
        
        error   = layer_2 - walk_vs_stop[i:i+1]     # 1
        layer_2_error += np.sum((layer_2 - walk_vs_stop[i:i+1]) ** 2)
        
        #layer_2_delta = (layer_2 - walk_vs_stop[i:i+1])
        #layer_1_delta=layer_2_delta.dot(weights_1_2.T)*relu2deriv(layer_1)
        
        delw_1_2 = error * layer_1.T     #(1,4)
        #delw_0_1  = (layer_0.dot(np.dot(error,weights_1_2))).T * relu2deriv(np.dot(weights_0_1,layer_0))
        delw_0_1  = (layer_0.dot(error.dot(weights_1_2) * relu2deriv((layer_1).T))).T #(3,1) (1,4)
            
        weights_1_2 -= alpha * delw_1_2
        weights_0_1 -= alpha * delw_0_1
    if(iteration % 10 == 9):
        print("Error:" + str(layer_2_error))