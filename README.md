
# Sprawozdanie nr 1

# Uruchomienie serwera 
python server.py -p (numer_portu)
# Budowa obrazu 
docker build . -t (nazwa)
# Uruchomienie kontenera 
docker run --rm -p <numer_portu_usługi>:3338 -it (nazwa)
# Warstwy 
sudo docker image inspect sprawozdanie_i -f '{{.RootFS.Layers}}
# Logi 
Logi przechowywane są w pliku `logs.txt` Wyświeltane są również po zamknięciu serwera
