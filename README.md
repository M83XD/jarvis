# Merhaba! Boş zamanlarımda yapmış olduğum ufak bir yapay zeka/asistan örneğimdir. Altta proje ile alakalı ufak bir bilgi verdim.

# Bu kod, bir konuşma tanıma asistanı oluşturur. Kullanıcı konuştuğunda, asistan metni anlamaya çalışır ve belirli komutları algılar. Kodun işleyişi şu şekildedir:

# speech_recognition kütüphanesi ile kullanıcının konuşmasını tanımak için mikrofondan ses alır.
# Kullanıcının söylediği metni Google'ın konuşma tanıma API'sıyla tanımaya çalışır.
# Tanınan metni ekrana yazar.
# Metinde belirli kelimeleri arar ve uygun yanıtları verir.
# Eğer metinde "nerede" geçiyorsa, Google Haritalar'da arama yapar ve sonucu açar.
# Kodun düzgün çalışabilmesi için datetime modülünü içe aktarmalısınız. Ayrıca, belirli bir yeri aramak için doğru formatta metin geçmeniz gerekir, yoksa web tarayıcısı düzgün çalışmaz.
