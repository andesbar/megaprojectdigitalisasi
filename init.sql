CREATE TYPE user_level AS ENUM ('nasional', 'provinsi', 'kabupaten', 'kecamatan', 'desa');

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL, -- Hasil hash_password()
    full_name VARCHAR(100),
    level user_level NOT NULL,

    -- Foreign Key yang fleksibel (NULL jika levelnya lebih tinggi)
    province_id CHAR(2) REFERENCES provinces(id),
    regency_id CHAR(4) REFERENCES regencies(id),
    district_id CHAR(7) REFERENCES districts(id),
    village_id CHAR(10) REFERENCES villages(id),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
