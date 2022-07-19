CREATE TABLE if not exists airports (
    iata text PRIMARY KEY,
    city text,
    country text
);

INSERT INTO airports
VALUES
    ("ORD", "Chicago", "United States"),
    ("JFK", "New York City", "United States"),
    ("CDG", "Paris", "France"),
    ("LHR", "London", "United Kingdom"),
    ("DME", "Moscow", "Russia"),
    ("SVO", "Moscow", "Russia")