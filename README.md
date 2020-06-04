# docker-deployment-with-flask
Gelistirilen makine ogrenmesi modelinin Docker Container yapisiyla deploy edilmesine ornek bir uygulamadir.


Model gelistirme surecini [ML-Deployment](https://github.com/hasanamanet/ML-Deployment/tree/master/modeling) adresinden inceleyebilirsiniz.


# Docker ile ilgili temel kavramlar: 
Docker'da olusturacaginiz container icin gerekli olan temel dosyalar sunlardir:
- model.pkl
- Dockerfile
- app.py
- requirements.txt
<br> seklindedir.
model.pkl: Gelistirdigimiz modelin kaydedildigi pickle dosyasi. <br>

Dockerfile: Docker kosturulacak Containerlarin yapisini olusturan her image bir Dockerfile ile tanimlanmasi gerekmektedir. Dockerfile icersinde image'in hangi image baz aldigi hangi dosyalari icerdigi ve hangi uygulamanin hangi parametrelerle calistiralacagi verilmektedir.<br>
app.py: Gelistirilen modelin canliya alinmasi Flask kodunun yer aldigi dosya.<br>
requirements.txt: Docker Containerde kosturulacak uygulamanin Python kodlarini sorunsuz sekilde calistirmasi icin ihtiyac duydugu Python kutuphanelerinin yer aldi txt dosyasi. (Bu dosya olusturulurken gelistirme ortaminda kullanilan kutuphanelerin surum bilgisinin de paylasilmasi faydali olacaktir. Ornegin; pandas==0.25.0 gibi)<br>
Son olarak uygulama docker-compose ile build edilim ayagi kaldirilacagi icin docker-compose.yml dosyasina ihtiyacimiz olacak. Bu dosya ile docker containerina hizmet olarak tanmlamamiz gereken hizmetleri tanimliyor ve gerekli olan parametreleri veriyoruz.

# Faydalandigim Kaynaklar:
- www.gokhansengun.com
- Online egitimler.

