# Fill in the matrices P, F, H, R and I at the bottom

from matrix import *

########################################

def calculate(measurements, initial_xy):
  dt = 0.1

  x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)
  u = matrix([[0.], [0.], [0.], [0.]]) # external motion

  ### fill this in: ###
  #P =  # initial uncertainty
  P = matrix([[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,1000.,0.],[0.,0.,0.,1000.]])
  #F =  # next state function
  F = matrix([[1.,0.,dt,0.],[0.,1.,0.,dt],[0.,0.,1.,0.],[0.,0.,0.,1.]])
  #H =  # measurement function
  H = matrix([[1.,0.,0.,0.],[0.,1.,0.,0.]])
  #R =  # measurement uncertainty
  R = matrix([[0.1,0.],[0.,0.1]])
  #I =  # identity matrix
  I = matrix([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]])

  def filter(x, P):
    for n in range(len(measurements)):
      
      # prediction
      x = (F * x) + u
      P = F * P * F.transpose()
      
      # measurement update
      Z = matrix([measurements[n]])
      y = Z.transpose() - (H * x)
      S = H * P * H.transpose() + R
      K = P * H.transpose() * S.inverse()
      x = x + (K * y)
      P = (I - (K * H)) * P
    return x, P
    
  return filter(x, P)
