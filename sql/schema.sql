-- ===========================
-- GreenGuardian v3.0 Schema
-- ===========================

DROP TABLE IF EXISTS health_logs CASCADE;
DROP TABLE IF EXISTS watering_logs CASCADE;
DROP TABLE IF EXISTS plant_knowledge CASCADE;
DROP TABLE IF EXISTS plants CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- USERS
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

-- PLANTS
CREATE TABLE plants (
    plant_id SERIAL PRIMARY KEY,
    plant_name VARCHAR(100) NOT NULL,
    plant_type VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    watering_frequency INTEGER NOT NULL,
    date_added DATE DEFAULT CURRENT_DATE
);

-- WATERING LOGS
CREATE TABLE watering_logs (
    log_id SERIAL PRIMARY KEY,
    plant_id INTEGER NOT NULL,
    watered_on DATE DEFAULT CURRENT_DATE,
    notes TEXT,

    CONSTRAINT fk_watering_plant
        FOREIGN KEY (plant_id)
        REFERENCES plants(plant_id)
        ON DELETE CASCADE
);

-- HEALTH LOGS
CREATE TABLE health_logs (
    health_log_id SERIAL PRIMARY KEY,
    plant_id INTEGER NOT NULL,
    status VARCHAR(100) NOT NULL,
    observed_on DATE DEFAULT CURRENT_DATE,
    notes TEXT,

    CONSTRAINT fk_health_plant
        FOREIGN KEY (plant_id)
        REFERENCES plants(plant_id)
        ON DELETE CASCADE
);

-- KNOWLEDGE CENTER
CREATE TABLE plant_knowledge (
    plant_type VARCHAR(100) PRIMARY KEY,
    scientific_name VARCHAR(150),
    importance TEXT,
    uses TEXT,
    sunlight_requirement TEXT,
    watering_tips TEXT
);