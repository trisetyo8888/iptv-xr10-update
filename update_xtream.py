import requests
import os

# Konfigurasi Xtream Codes (Ganti dengan detail Anda atau gunakan GitHub Secrets)
URL = "http://poseidon.neorpahe.top:8080/"
USERNAME = "3571790698170"
PASSWORD = "613a3d618652"

def fetch_xtream_data():
    # Mengambil playlist M3U dari Xtream Codes
    playlist_url = f"{URL}/get.php?auth={USERNAME}&auth_password={PASSWORD}&output=ts"
    
    try:
        print("Mengunduh data dari Xtream Codes...")
        response = requests.get(playlist_url, timeout=30)
        
        if response.status_code == 200:
            # Menyimpan hasil ke file playlist.m3u
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("File playlist.m3u berhasil diperbarui!")
        else:
            print(f"Gagal mengambil data. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    fetch_xtream_data()
