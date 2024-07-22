                    Google Dorking Aracı
                    
Google Dorking Aracı, Google aramalarında daha spesifik ve etkili sonuçlar elde etmenizi sağlayan bir Python programıdır. Bu araç, siber güvenlik araştırmalarında ve bilgi toplama süreçlerinde kullanışlı olabilir. Program, Google'ın arama motorunu belirli dork komutları ve sorgular ile hedeflenmiş şekilde kullanmanıza olanak tanır.

Özellikler
ASCII Sanatı: Programın başlangıcında görsel bir karşılama sağlar.

Şifre Koruma: Programı kullanmak için belirli bir şifre gerektirir, böylece yalnızca yetkili kullanıcılar erişebilir.

Hata Yönetimi ve Yeniden Deneme: HTTP istekleri sırasında karşılaşılan hataları yönetir ve yeniden deneme mekanizması sunar.

Google Dorking: Kullanıcı tarafından sağlanan sorgular ile Google'da arama yapar ve sonuçları toplar.

Sonuçları Yazdırma: Arama sonuçlarını kullanıcı dostu bir formatta ekrana yazdırır.

Kullanıcı Sorguları: Komut satırından veya etkileşimli olarak kullanıcı sorgularını alır.

Kurulum

Python Yükleyin: Python 3.x sürümünün yüklü olduğundan emin olun.

Gerekli Kütüphaneleri Kurun: requests, beautifulsoup4, argparse, getpass gibi kütüphaneleri kurmanız gerekiyor. Bunu yapmak için:

pip install requests beautifulsoup4

Kullanım
Şifre ile Erişim: Programı çalıştırmadan önce şifreyi doğru girmeniz gerekmektedir.

Komut Satırı Argümanları: Google dorking sorgularını komut satırından geçirebilir veya etkileşimli olarak girebilirsiniz.


python google_dorking.py --queries "site:example.com" 
"filetype:pdf"
veya

python google_dorking.py

Bu komutları kullanarak sorgularınızı etkileşimli olarak girebilirsiniz.

Sonuçları Görüntüleme: Program arama sonuçlarını başlık, bağlantı ve özet ile birlikte ekrana yazdırır.

Katkıda Bulunma

Katkıda bulunmak isteyenler için:

Pull request'ler ve öneriler her zaman memnuniyetle karşılanır.
Sorunlar ve hata raporları için Issues sayfasını kullanabilirsiniz.
Proje ile ilgili her türlü geri bildirim ve öneri için Discussions bölümünü ziyaret edebilirsiniz.

