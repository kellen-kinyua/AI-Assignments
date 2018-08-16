import random

x = [1,2,3,4,5]
y = []
y_curr = 1
m_curr = 1
b_curr = 1
cost = 0
m_grad = 0
b_grad = 0
learning_rate = 0.001

for i in range(5):
    y.append(random.randint(1,10))
print (y)

N = float(len(y))

for i in range(100):
    y_curr = (m_curr * x[i]) + b_curr
    cost+=((y[i]-y_curr))**2/N
    sumValues_m_grad = 0
    sumValues_b_grad = 0
    for t in range(len(x)):
        sumValues_m_grad+= (x[t] *(y[t] - y_curr))
        sumValues_b_grad+= (y[t] - y_curr)
    
    m_grad = -(2/N) * sumValues_m_grad
    b_grad = -(2/N) * sumValues_b_grad

    m_curr = m_curr- (learning_rate * m_grad)
    b_curr = b_curr- (learning_rate * b_grad)

print(m_curr, b_curr, cost)
                          


