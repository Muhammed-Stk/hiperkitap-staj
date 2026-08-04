import time

print("Merhaba!")

# 5'ten geriye sayan basit bir döngü
for i in range(5, 0, -1):
    print(f"Konteynerin kapanmasına {i} saniye kaldı...")
    time.sleep(1)

print("\nİşlem başarıyla tamamlandı. Hoşçakal!")