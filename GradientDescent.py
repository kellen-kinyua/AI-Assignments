def linear_regression(X, y, m_current=0, b_current=0, epochs=1000, learning_rate=0.0001):
     N = float(len(y))
     data = 1
     for i in range(epochs):
          y_current = (m_current * X[i]) + b_current
          cost = sum([data**2 for data in (y[data]-y_current)]) / N
          m_gradient = -(2/N) * sum(X[i] * (y[i] - y_current))
          b_gradient = -(2/N) * sum(y[i] - y_current)
          m_current = m_current - (learning_rate * m_gradient)
          b_current = b_current - (learning_rate * b_gradient)
     return m_current, b_current, cost


x = [1, 1, 2, 3, 4, 3, 4, 6, 4]
y = [2, 1, 0.5, 1, 3, 3, 2, 5, 4]
print (linear_regression(x,y))
