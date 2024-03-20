"""
# 1) arp request
# 2) broadcast
# 3) arp response
"""
"""
scapy.ls(scapy.[Method]()) komutuyla paketin icerisindeki methodlari gorebiliriz.
1-) scapy.ARP ile "pdst" komutunu kullanarak ip bloguna ARP istegi gonderdik. Ve bunu bir degiskene atadik.
2-) scapy.Ether ile "dst" komutunu kullanarak Modeme broadcast istegi gonderdik. Ve bunu bir degiskene atadik.
3-) Broadcast paketiyle arp request paketini birlestiriyoruz. Ve bunu bir degiskene atiyoruz. broadcast ile arp in birlestirilmesinin sebebi ise tek bir pakette toplayarak ikisinin ayni anda mac adresine iletilmesi.
4-) scapysrp({gonderilmek istenen packet}, {timeout=0}) "timeout=1" cevap alinmadiysa yani response gelmediyse "timeout=1" deger kadar bekler.
5-) tuple yardimiyla hem cevap gelenlerin listesini hemde cevap gelmeyenleri ayni tuple icerisindde degisken yaptik.
6-) "answer_list" cevap verenlerin listesini "answer_list.summary()" ile scapynin kendi icerisinde olan ozellik ile kisa bir liste yaptik. yani summary() bize basit bir sekilde answer listesini duzenledi.
"""
import scapy.all as scapy
arp_request_packet = scapy.ARP(pdst="192.168.80.0/24")
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
combined_packet = broadcast_packet / arp_request_packet
(answer_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
answer_list.summary()