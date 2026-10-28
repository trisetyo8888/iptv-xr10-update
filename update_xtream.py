import os
import requests

# Mengambil konfigurasi dari GitHub Secrets demi keamanan
# Jika ingin tes lokal, Anda bisa mengganti os.environ.get dengan string manual, contoh: URL = "http://domain.com:8080"
URL = os.environ.get("XTREAM_URL", "http://poseidon.neorpahe.top:8080")
USERNAME = os.environ.get("XTREAM_USER", "3571790698170")
PASSWORD = os.environ.get("XTREAM_PASS", "613a3d618652")

def fetch_xtream_data():
    # Menggunakan format m3u_plus yang umumnya lebih stabil diterima server
    playlist_url = f"{URL}/get.php?auth={USERNAME}&auth_password={PASSWORD}&output=ts&type=m3u_plus"
    
    # Header browser palsu untuk melewati proteksi firewall/bot server Xtream Codes
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    
    try:
        print("Sedang menyambungkan ke server Xtream Codes...")
        response = requests.get(playlist_url, headers=headers, timeout=45)
        
        # Mengecek apakah data berhasil diambil
        if response.status_code == 200:
            # Memastikan isi respon tidak kosong atau tidak berisi teks error
            if "INVALID CREDENTIALS" in response.text.upper() or "UNAUTHORIZED" in response.text.upper():
                print("Gagal: Server merespon 200, tetapi teks berisi 'Unauthorized'. Periksa kembali Username/Password.")
                return

            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Sukses! File playlist.m3u berhasil diperbarui dan disimpan.")
            
        else:
            print(f"Gagal mengambil data. Status code: {response.status_code}")
            print("Catatan: Jika tetap 401, periksa kembali URL, Username, dan Password Anda.")
            
    except requests.exceptions.Timeout:
        print("Gagal: Waktu koneksi habis (Timeout). Server tujuan lambat atau memblokir IP GitHub.")
    except Exception as e:
        print(f"Terjadi kesalahan sistem: {e}")

if __name__ == "__main__":
    fetch_xtream_data()













