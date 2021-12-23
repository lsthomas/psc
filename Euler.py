import numpy as np
import matplotlib.pyplot as plt

def F0(r,y):
  return np.array([y[1],-1/(r**2-r)*(y[1]+y[0]*(1-y[0]**2))])

def euler(a,n,r_max):
  h = (r_max-1)/n
  b = a*(1-a**2)
  c = (b*(1-3*(a**2)))/2
  y0 = np.array([a,b])
  r0 = 1
  y=y0
  r=r0
  Y = [y0]
  R = [r0]
  y1 = np.array([a+h*b,b+h*c])
  y = y1
  r = 1+h
  R = [r0, r0+h]
  Y = [y0,y1]
  for k in range(n) :
    if abs(y[0]) < 1.001 :
      y = y + h*F0(r,y)
      r = r+h
      Y.append(y)
      R.append(r)
  return R,Y


def graphique_euler(a, n, r_max):
    R, Y = euler(a, n, r_max)
    Y_vrai = []
    for e in Y:
        Y_vrai.append(e[0])

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.ylim([-1, 1])

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ##ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ##ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ##ax.xaxis.set_t£icks_position('bottom')
    ##ax.yaxis.set_ticks_position('left')

    # Légende
    plt.plot(R, Y_vrai, label="a=" + str(a)[0:8])
    ax.legend(loc="best")
