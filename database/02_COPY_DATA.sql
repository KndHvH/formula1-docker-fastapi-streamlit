

COPY DRIVERS FROM '/data/drivers.csv' DELIMITER ',' CSV HEADER;
COPY FASTEST_LAPS FROM '/data/fastest_laps.csv' DELIMITER ',' CSV HEADER;
COPY RACES FROM '/data/races.csv' DELIMITER ',' CSV HEADER;