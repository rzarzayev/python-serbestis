import matplotlib.pyplot as plt

# Hücum məlumatları (nümunə)
data = {
    "IP": ["192.168.1.1", "10.0.0.2", "172.16.0.3"],
    "Hits": [5, 10, 3]
}

def plot_attack_data(data):
    plt.bar(data["IP"], data["Hits"], color="blue")
    plt.xlabel("IP Ünvanları")
    plt.ylabel("Hücum Sayı")
    plt.title("Honeypot Hücum Məlumatları")
    plt.show()

# Nümunə qrafik
plot_attack_data(data)
