import requests
from bs4 import BeautifulSoup
import urllib.parse
import random
import logging
import argparse
import getpass
import time

# Yeni ASCII Sanatı
ascii_art = '''
 ██▀███     ▓█████     ██ ▄█▀     ██████    ▓██   ██▓
▓██ ▒ ██▒   ▓█   ▀     ██▄█▒    ▒██    ▒     ▒██  ██▒
▓██ ░▄█ ▒   ▒███      ▓███▄░    ░ ▓██▄        ▒██ ██░
▒██▀▀█▄     ▒▓█  ▄    ▓██ █▄      ▒   ██▒     ░ ▐██▓░
░██▓ ▒██▒   ░▒████▒   ▒██▒ █▄   ▒██████▒▒     ░ ██▒▓░
░ ▒▓ ░▒▓░   ░░ ▒░ ░   ▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░      ██▒▒▒ 
  ░▒ ░ ▒░    ░ ░  ░   ░ ░▒ ▒░   ░ ░▒  ░ ░    ▓██ ░▒░ 
  ░░   ░       ░      ░ ░░ ░    ░  ░  ░      ▒ ▒ ░░  
   ░           ░  ░   ░  ░            ░      ░ ░     
                                             ░ ░     
'''

# Şifre kontrolü
def sifre_kontrol():
    dogru_sifre = "turkhackteam"
    for _ in range(3):
        girilen_sifre = getpass.getpass("Lütfen şifreyi girin: ")
        if girilen_sifre == dogru_sifre:
            print("Şifre doğru, erişim izni verildi.")
            return True
        else:
            print("Şifre yanlış, tekrar deneyin.")
    print("Çok fazla başarısız girişim, program sonlandırılıyor.")
    return False

# Günlük ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hata yönetimi ve yeniden deneme mantığı
def yeniden_dene(url, headers, retries=3):
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.warning(f"{url} çekme hatası: {e}")
            time.sleep(5)
    return None

# Google Dork işlemi
def google_dork(query, num_results=10):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    ]
    headers = {"User-Agent": random.choice(user_agents)}
    
    response = yeniden_dene(url, headers)
    if response is None:
        logging.error(f"Sorgu için sonuçlar alınamadı: {query}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    for g in soup.find_all('div', class_='g'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text if g.find('h3') else "Başlık yok"
            snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else "Özet yok"
            results.append({"title": title, "link": link, "snippet": snippet})
    
    return results

# Sonuçları ekrana yazdır
def yazdir_sonuclar(results):
    for result in results:
        print(f"Başlık: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Özet: {result['snippet']}\n")
        print("-" * 80 + "\n")

# Kullanıcıdan dorking sorguları al
def al_kullanici_sorgulari():
    queries = []
    print("Google Dorking sorgularınızı girin (bitirmek için 'done' yazın):")
    while True:
        query = input("> ")
        if query.lower() == 'done':
            break
        queries.append(query)
    return queries

# Ana fonksiyon
def main():
    # Başlangıçta ASCII sanatını yazdır
    print(ascii_art)
    time.sleep(5)  # Kodun işleyişi 5 saniye bekle

    if not sifre_kontrol():
        return

    parser = argparse.ArgumentParser(description="Basit Google Dorking Aracı")
    parser.add_argument('--queries', nargs='+', help='Google Dorking sorgularının listesi', default=None)
    args = parser.parse_args()
    
    user_queries = args.queries if args.queries else al_kullanici_sorgulari()
    
    for query in user_queries:
        results = google_dork(query)
        yazdir_sonuclar(results)
        logging.info(f"Sorgu işlendi: {query}")

if __name__ == "__main__":
    main()