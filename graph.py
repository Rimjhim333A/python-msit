import numpy as np
import matplotlib.pyplot as plt
class Graph:
    def RandomArrayGraph():
        x_axis = np.random.randint(10,90,12)
        y_axis= np.random.randint(50,120,12)
        # x_axis-np.array_split(x_axis,2)
        # y_axis-np.array_split(y_axis,2)
        print(x_axis,type(x_axis),len(x_axis))
        print(y_axis,type(y_axis),len(y_axis))
        plt.plot(x_axis,y_axis,marker="o",mfc="red",mec="red",color="blue")
        plt.plot(x_axis,marker="o",mfc="red",mec="red",color="blue")
        plt.plot(y_axis,marker="o",mfc="red",mec="red",color="blue")
Graph.RandomArrayGraph()