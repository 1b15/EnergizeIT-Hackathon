import numpy as np
def classify_device(model, power_history):
    # power_history: float list, size 4
    # returns: probabilities of devices as list of floats: iphone, oneplus, laptop, ventilator1, ventilator2, ventilator3
    if power_history[-1] == 0:
        return [0, 0, 0, 0, 0, 1]
    else:
        x = model.predict(np.array([[power_history]]))[0]
        probs = (x / np.sum(x, axis=0)).tolist()
        probs.append(0)
    return probs