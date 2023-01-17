BEGIN;

DO
$do$
DECLARE
    current_migration_number integer := 2;
BEGIN
    IF NOT EXISTS (SELECT migration_number FROM migrations WHERE migration_number = current_migration_number) THEN
        CREATE EXTENSION IF NOT EXISTS citext;
        CREATE TABLE articles (
            id SERIAL PRIMARY KEY,
            page_id INT NOT NULL UNIQUE,
            title CITEXT NOT NULL,
            article_extract CITEXT,
            thumbnail_image_url CITEXT,
            created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMPTZ
        );

        INSERT INTO migrations(migration_number) VALUES (current_migration_number);
    ELSE
        RAISE NOTICE 'Already ran migration %.', current_migration_number;
    END IF;
END
$do$;

COMMIT;
