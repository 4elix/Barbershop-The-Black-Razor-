try:
    from .tools_sql import SQLBaseConnect
except ImportError:
    from tools_sql import SQLBaseConnect


class CreateTableBasic(SQLBaseConnect):
    def ctb_users(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                profile_path TEXT,
                role TEXT CHECK (role IN ('admin', 'client')),
                language TEXT,
                tg_id BIGINT NOT NULL UNIQUE
            );
        '''
        self.manager(sql, commit=True)


class CreateTableService(SQLBaseConnect):
    def cts_categories(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS categories(
                category_id SERIAL PRIMARY KEY,
                name_category TEXT
            );
        '''
        self.manager(sql, commit=True)

    def cts_services(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS services(
                service_id SERIAL PRIMARY KEY,
                name_service TEXT,
                price NUMERIC(10, 2),
                description TEXT,
                image_path TEXT,
                category_id INTEGER REFERENCES categories(category_id) ON DELETE SET NULL
            );
        '''
        self.manager(sql, commit=True)

    def cts_order_services(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS order_services(
                os_id SERIAL PRIMARY KEY,
                service_id INTEGER REFERENCES services(service_id) ON DELETE SET NULL,
                user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
                total_price NUMERIC(10, 2),
                total_service INTEGER,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            );
        '''
        self.manager(sql, commit=True)


class DropTableAll(SQLBaseConnect):
    def drop_table(self):
        sql = 'DROP TABLE IF EXISTS users, categories, services, order_services CASCADE;'
        self.manager(sql, commit=True)