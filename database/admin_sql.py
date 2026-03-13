try:
    from .tools_sql import SQLBaseConnect
except ImportError:
    from tools_sql import SQLBaseConnect


class CreateObjectsForServices(SQLBaseConnect):
    def cofs_categories(self, name_category: str):
        sql = '''
            INSERT INTO categories(name_category) 
            VALUES (%s)
        '''
        self.manager(sql, name_category, commit=True)

    def cofs_services(self, name_service: str, price: float, description: str, image_path: str, category_id: int):
        sql = '''
            INSERT INTO services(name_service, price, description, image_path, category_id)
            VALUES (%s, %s, %s, %s, %s)
        '''
        self.manager(sql, name_service, price, description, image_path, category_id, commit=True)


