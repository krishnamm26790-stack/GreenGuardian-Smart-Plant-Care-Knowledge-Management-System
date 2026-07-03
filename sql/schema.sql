CREATE TABLE plants (

    plant_id SERIAL PRIMARY KEY,

    plant_name VARCHAR(100) NOT NULL,

    plant_type VARCHAR(50) NOT NULL,

    location VARCHAR(100),

    watering_frequency INTEGER NOT NULL,

    date_added DATE DEFAULT CURRENT_DATE

);