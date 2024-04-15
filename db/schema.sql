CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) UNIQUE NOT NULL,
      password VARCHAR(50) NOT NULL,
      email VARCHAR(50) UNIQUE NOT NULL,
      active BOOLEAN DEFAULT TRUE,
      role VARCHAR(50) NOT NULL
);

CREATE TABLE children (
      id SERIAL PRIMARY KEY,
      first_name VARCHAR(255) NOT NULL,
      last_name VARCHAR(255) NOT NULL,
      community VARCHAR(255) NOT NULL,
      -- dob VARCHAR(255),
      -- consent BOOLEAN,
      -- allergies TEXT,
      -- created_by INTEGER REFERENCES users(id) ON DELETE CASCADE,
      created_at TIMESTAMP DEFAULT NOW(),
      active BOOLEAN DEFAULT TRUE
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    day VARCHAR NOT NULL,
    community VARCHAR(255) NOT NULL,
    child VARCHAR(255),
    cycle INTEGER NOT NULL,
    attendance BOOLEAN
);


