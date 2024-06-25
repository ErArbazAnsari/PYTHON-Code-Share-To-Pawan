import matplotlib.pyplot as plt

data1 = ['cse1', 'cse2', 'cse3','cse1', 'cse2', 'cse3']
data2 = [10,15,20,100,200,500]

plt.pie(data2, labels=data1,autopct="%1.1f%%")
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.show()