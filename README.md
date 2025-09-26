 IMDb Qdrant Recommender

Türkçe Açıklama

Bu proje, IMDb film verilerini kullanarak **Qdrant** tabanlı bir öneri sistemi geliştirmek için hazırlanmıştır.  
Backend tarafında **Python (FastAPI)**, frontend tarafında ise basit bir web arayüzü ve **Nginx** kullanılmıştır.  

 Özellikler
- IMDb film verilerini Qdrant vektör veritabanına indexleme  
- Benzerlik tabanlı film önerileri  
- Docker Compose ile kolay kurulum  
- Basit frontend arayüzü  

 Kurulum
Projeyi bilgisayarınıza klonladıktan sonra:  

```bash
git clone https://github.com/irem864/imdb-qdrant-recommender.git
cd imdb-qdrant-recommender
docker-compose up --build

backend/       -> FastAPI uygulaması
nginx/         -> Frontend ve Nginx ayarları
docker-compose.yml -> Servislerin orkestrasyonu

Tarayıcınızdan http://localhost:8080 adresine giderek öneri sistemini deneyebilirsiniz.
English Description

This project is a Qdrant-based recommendation system built using IMDb movie data.
It uses Python (FastAPI) on the backend, and a simple web interface with Nginx on the frontend.

 Features

Indexing IMDb movie data into Qdrant vector database

Similarity-based movie recommendations

Easy setup with Docker Compose

Simple frontend UI

 Installation

Clone the repository and run:

git clone https://github.com/irem864/imdb-qdrant-recommender.git
cd imdb-qdrant-recommender
docker-compose up --build

 Project Structure
backend/       -> FastAPI app
nginx/         -> Frontend and Nginx configs
docker-compose.yml -> Orchestration of services

 Usage

Open http://localhost:8080 in your browser to test the recommender system.
