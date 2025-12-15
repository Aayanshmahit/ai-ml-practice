import matplotlib.pyplot as plt
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'others']
usage = [30, 20, 10, 10, 7, 15]
plt.pie(usage, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title("Programming Language Usage (Crowded Example)")
plt.show()