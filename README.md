# Crypto Price Monitor

Una aplicación para monitorear los precios de las criptomonedas desarrollada con Python, MySQL y MongoDB.

## Descripción general

Este proyecto recupera los precios de las criptomonedas a través de la API de CoinGecko, almacena registros históricos en bases de datos relacionales y NoSQL, y ofrece herramientas para consultar y analizar los datos de precios.

El objetivo es construir una herramienta que permita recopilar, almacenar, consultar y analizar información del mercado de criptomonedas, aplicando conceptos de programación, consumo de APIs, gestión de bases de datos y análisis de datos.

## Contexto académico

Este proyecto forma parte de mi proceso de formación en el programa **Data Science Jr. de Tecnolochicas Pro**, impulsado por **Fundación Televisa**.

Surge como parte de las actividades prácticas y postworks del programa, en los que he podido aplicar y reforzar conocimientos sobre Python, consumo de APIs y bases de datos.

Este repositorio representa una evolución personal del trabajo académico original: busca ampliar sus funcionalidades, mejorar su arquitectura y convertirlo en un proyecto práctico para mi aprendizaje y portafolio profesional.

Mi agradecimiento a **Tecnolochicas Pro y Fundación Televisa** por impulsar oportunidades de formación para mujeres en las áreas STEM, así cómo abrir caminos en el mundo de la ciencia y la tecnología!

## Pila tecnológica

- Python 3.13
- API de CoinGecko
- MySQL
- MongoDB
- PyMongo
- Pandas
- Matplotlib
- Pytest

## Estructura del proyecto

```text
crypto-price-monitor/
├── notebooks/
├── sql/
├── src/
│   ├── api/
│   ├── analytics/
│   ├── database/
│   └── services/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Funcionalidades actuales

- [x] Configuración del entorno de Python
- [x] Conexión a MongoDB
- [x] Conexión a MySQL
- [x] Inicialización de la base de datos
- [ ] Integración de la API de CoinGecko
- [ ] Recopilación de precios de criptomonedas
- [ ] Consultas de precios históricos
- [ ] Análisis estadístico y visualizaciones

## Configuración

Clona el repositorio:

```bash
git clone TU_URL_DEL_REPOSITORIO
cd crypto-price-monitor
```

Crea y activa un entorno virtual, luego instala las dependencias:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configura tu archivo `.env` usando `.env.example` como referencia.

## Estado

Actualmente en desarrollo.

## Reconocimientos

Este proyecto tiene como punto de partida una actividad práctica realizada durante mi formación en **Data Science Jr. con Tecnolochicas Pro y Fundación Televisa**.

El desarrollo, las mejoras y las ampliaciones de este repositorio forman parte de mi proceso de aprendizaje y crecimiento profesional en el área de ciencia de datos.
