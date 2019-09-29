import numpy as np
def classify_device(power_history):
  # power_history: float list, size 4
  # returns: probabilities of devices as list of floats: iphone, oneplus, laptop, ventilator1, ventilator2, ventilator3, nuffin
  x = np.random.normal(0, 1, 6)
  probs = np.exp(x) / np.sum(np.exp(x), axis=0)
  return list(probs)