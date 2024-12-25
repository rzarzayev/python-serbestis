import seaborn as sns
import pandas as pd

# Hücum məlumatları
data = pd.DataFrame({
    "IP": ["192.168.1.1", "10.0.0.2", "172.16.0.3"],
    "Hits": [5, 10, 3]
})

def visualize_data(df):
    sns.barplot(x="IP", y="Hits", data=df)
    plt.title("Honeypot Hücumları")
    plt.show()

# Vizualizasiya
visualize_data(data)
