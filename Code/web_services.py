import requests
import matplotlib.pyplot as plt
r = requests.get("http://pulse.suyash.io/api/list")
r2 = requests.get("http://pulse.suyash.io/api/pulse/56fa32ce88b0f17d50e08a23")
plt.figure()
parsed_data = r2.json()
plt.plot(parsed_data['pulse_data'])
plt.show()