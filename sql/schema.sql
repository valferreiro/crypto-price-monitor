CREATE DATABASE IF NOT EXISTS crypto_monitor;
USE crypto_monitor;

CREATE TABLE IF NOT EXISTS price_history (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,

    coin_id VARCHAR(50) NOT NULL,
    symbol VARCHAR(15) NOT NULL,
    name VARCHAR(100) NOT NULL,

    price DECIMAL(24, 10) NOT NULL,
    currency VARCHAR(10) NOT NULL,

    recorded_at DATETIME(6) NOT NULL,
    source VARCHAR(50) NOT NULL,

    market_cap DECIMAL(30, 10),
    total_volume DECIMAL(30, 10),
    price_change_percentage_24h DECIMAL(12, 6),

    INDEX idx_coin_recorded (coin_id, recorded_at),
    INDEX idx_symbol (symbol)
);