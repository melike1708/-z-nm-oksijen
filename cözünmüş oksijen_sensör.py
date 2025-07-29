import random
import time

def simulate_dissolved_oxygen():
    # Çözünmüş oksijen seviyesi 0 ile 20 mg/L arasında rastgele bir değer oluştur.
    dissolved_oxygen_level = round(random.uniform(0, 20), 2)  # 0 to 20 mg/L
    return dissolved_oxygen_level

try:
    while True:
        # Çözünmüş oksijen için simülasyonu yap.
        simulated_dissolved_oxygen = simulate_dissolved_oxygen()

        # Simüle edilen çözünmüş oksijen konsantrasyonunu yazdır.
        print(f"Simulated Dissolved Oxygen Level: {simulated_dissolved_oxygen} mg/L")

        # 1 saniye bekle.
        time.sleep(1)

except KeyboardInterrupt:
    print("Simülasyon durduruldu.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
