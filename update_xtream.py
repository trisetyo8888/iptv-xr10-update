import os
import requests

URL = os.environ.get("XTREAM_URL", "http://poseidon.neorpahe.top:8080")
USERNAME = os.environ.get("XTREAM_USER", "3571790698170")
PASSWORD = os.environ.get("XTREAM_PASS", "613a3d618652")

def try_fetch(url, description):
    # Menggunakan User-Agent TiviMate yang dipercaya oleh server Xtream Codes
    headers = {
        'User-Agent': 'TiviMate/4.7.0 (Linux; Android 11)',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    try:
        print(f"Mencoba {description}...")
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Cegah respon tipuan yang berisi teks error di dalam status 200
            if "INVALID CREDENTIALS" in response.text.upper() or "UNAUTHORIZED" in response.text.upper():
                print(f"-> Gagal {description}: Server merespon 200 tetapi teks berisi 'Unauthorized'.")
                return None
                
            print(f"-> BERHASIL menggunakan {description}!")
            return response.text
        else:
            print(f"-> Gagal {description}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"-> Error pada {description}: {e}")
        return None

def fetch_xtream_data():
    # 3 Variasi URL Endpoint Xtream Codes yang paling sering diterima server
    endpoints = [
        {
            "url": f"{URL}/get.php?auth={USERNAME}&auth_password={PASSWORD}&output=ts",
            "desc": "Metode Standard (get.php)"
        },
        {
            "url": f"{URL}/get.php?username={USERNAME}&password={PASSWORD}&output=ts&type=m3u_plus",
            "desc": "Metode M3U Plus"
        },
        {
            "url": f"{URL}/player_api.php?username={USERNAME}&password={PASSWORD}",
            "desc": "Metode Player API (JSON)"
        }
    ]
    
    playlist_content = None
    
    # Loop untuk mencoba semua metode hingga salah satu berhasil
    for endpoint in endpoints:
        playlist_content = try_fetch(endpoint["url"], endpoint["desc"])
        if playlist_content:
            # Jika berhasil, tentukan nama file berdasarkan output (M3U atau JSON)
            filename = "playlist.json" if "player_api.php" in endpoint["url"] else "playlist.m3u"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(playlist_content)
            print(f"Sukses! File {filename} berhasil disimpan.")
            return

    # Jika semua metode melempar error
    print("\n[KESIMPULAN EROR 401]:")
    print("1. Periksa kembali keaslian isi Github Secrets Anda (apakah ada spasi terikut?).")
    print("2. Server Xtream Codes Anda memblokir IP server GitHub Actions secara total.")
    print("Solusi alternatif: Skrip ini harus dijalankan di VPS pribadi / PC lokal menggunakan Cron Job, bukan di GitHub.")

if __name__ == "__main__":
    fetch_xtream_data()

