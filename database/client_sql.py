try:
    from .tools_sql import SQLBaseConnect
except ImportError:
    from tools_sql import SQLBaseConnect


class BasicSqlRequest(SQLBaseConnect):
    def register_user(self, first_name: str, last_name: str, age: int,
                      profile_path: str, role: str, language: str, tg_id: int):
        sql = '''
            INSERT INTO users(first_name, last_name, age, profile_path, role, language, tg_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        self.manager(sql, first_name, last_name, age, profile_path, role, language, tg_id, commit=True)

    def check_registration(self, tg_id: int):
        sql = 'SELECT first_name FROM users WHERE tg_id = %s'
        name = self.manager(sql, tg_id, fetchone=True)[0]
        return name
