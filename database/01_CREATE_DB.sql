

CREATE TABLE DRIVERS (
    DSC_POSITION VARCHAR(40),
    DSC_DRIVER_NAME VARCHAR(40),
    DSC_DRIVER_NSC VARCHAR(3),
    DSC_CAR_TYPE VARCHAR(40),
    NUM_POINTS NUMERIC,
    NUM_YEAR INTEGER
);




CREATE TABLE FASTEST_LAPS (
    DSC_GP VARCHAR(40),
    DSC_DRIVER VARCHAR(40),
    DSC_CAR_TYPE VARCHAR(40),
    NUM_TIME TIME,
    NUM_YEAR INTEGER
);



CREATE TABLE RACES (
    DSC_GP VARCHAR(40),
    DAT DATE,
    DSC_WINNER VARCHAR(40),
    DSC_CAR_TYPE VARCHAR(40),
    NUM_TOTAL_LAPS INTEGER,
    NUM_TOTAL_LAP_TIME VARCHAR(40),
    NUM_YEAR INTEGER
);