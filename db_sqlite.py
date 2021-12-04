import sqlite3

# Fonte: https://stackoverflow.com/questions/1884818/how-do-i-add-a-foreign-key-to-an-existing-sqlite-table

class DatabaseManager:

    def __init__(self):
        self.db_name = None
        self.sql = ""
        self.datas_tuple = None
        self.has_values = False


    def connect(self, name):
        try:
            # instrução de criação 
            self.connection = sqlite3.connect(name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES )
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print("Erro:\n:", error)
            
        if self.connection:
            return self.connection
        else:
            return None
            
    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def executeSQL(self):

        try:
            if self.has_values:
                self.cursor.execute(self.sql, self.datas_tuple)
                self.clear_attributes()
            else:
                self.cursor.execute(self.sql)
            self.connection.commit()

            return 0
        
        except sqlite3.IntegrityError as erro:
            showerror("ERRO", "Erro:\n  {}".format(erro))
            
    def clear_attributes(self):
        #self.sql = ""
        self.datas_tuple = None
        self.has_values = False
        
    def create_table(self, tb_name, schema=False, fields=None, with_pk_id=True, with_autoincrement=True):
        if schema:
            self.sql = f"CREATE TABLE IF NOT EXISTS {schema}.{tb_name} ("
        else:
            self.sql = f"CREATE TABLE IF NOT EXISTS {tb_name} ("

        if with_pk_id:
            self.sql += "id INTEGER NOT NULL PRIMARY KEY"

        if with_autoincrement:
            self.sql += " AUTOINCREMENT"

        FOREIGNKEY_LIST = []

        # Each element/field on list named 'fields', must represent a field as dict 
        #field = {
        #    'name':'',
        #    'type': None, # String (i.e: 'Varchar')
        #    'argument':'', # String (i.e: '(100)')
        #    'default_value': '', # String (i.e: 'Jhon Doe')
        #    'unique': False,
        #    'not_null': False,
        #    'is_foreignkey': False,
        #    'reference_table': None, # <table_name>
        #    'reference_table_field': None, #(i.e: id)
        #}
        if fields is not None and isinstance(fields, list):
            for field in fields:
                column_def_args = ""
                if isinstance(field, dict):
                    if 'is_foreignkey' in field.keys() and field['is_foreignkey']:
                        FOREIGNKEY_LIST.append(f"FOREIGN KEY({field['name']}) REFERENCES {field['reference_table']}({field['reference_table_field']})")

                    column_def_args += field['name']
                    if 'type' in field.keys() and field['type']:
                        column_def_args += f" {field['type']}"

                    if 'argument' in field.keys() and field['argument'] != '':
                        column_def_args += f" {field['argument']}"

                    if 'unique' in field.keys() and field['unique']:
                        column_def_args += ' UNIQUE'

                    if 'not_null' in field.keys() and field['not_null']:
                        column_def_args += ' NOT NULL'

                    if 'default_value' in field.keys() and field['default_value'] != '':
                        column_def_args += f" DEFAULT {field['default_value']}"

                    self.sql += f", {column_def_args}"

            if len(FOREIGNKEY_LIST) > 0:
                for fk in FOREIGNKEY_LIST:
                    self.sql += f", {fk}"

        self.sql += ");"

        return True if self.executeSQL() == 0 else False
        
    def add_column(self, tb_name, fields=None):

        if fields is not None and isinstance(fields, list):

            for field in fields:
                self.sql = f"ALTER TABLE {tb_name} ADD COLUMN"
                column_add_args = ""
                if isinstance(field, dict):
                    
                    column_add_args += field['name']

                    if 'type' in field.keys() and field['type']:
                        column_add_args += f" {field['type']}"

                    if 'argument' in field.keys() and field['argument'] != '':
                        column_add_args += f" {field['argument']}"

                    if 'is_foreignkey' in field.keys() and field['is_foreignkey']:
                        column_add_args += f" REFERENCES {field['reference_table']}({field['reference_table_field']})"
                    else:
                        if 'unique' in field.keys() and field['unique']:
                            column_add_args += ' UNIQUE'

                        if 'not_null' in field.keys() and field['not_null']:
                            column_add_args += ' NOT NULL'

                        if 'default_value' in field.keys() and field['default_value'] != '':
                            column_add_args += f" DEFAULT {field['default_value']}"

                    self.sql += f" {column_add_args}"

                    self.sql += ";"
                    self.executeSQL()
            
        else:
            return False

    def insert_values(self, tb_name, values=None):

        # Each element/value on list named 'values', must represent a record as dict with multiples, or no, column name and value
        #element = {
        #    '<column_name>': <value>,
        #    '<column_name>': <value>,
        #}

        if isinstance(values, list):
            for value in values:
                self.sql = f"INSERT INTO {tb_name} ("
                if isinstance(value, dict):
                    self.has_values = True
                    cols = value.keys()
                    
                    self.datas_tuple = ()

                    cont_values = 0
                    for col in cols:
                        self.sql += f"'{col}', "
                        self.datas_tuple += (value[col],)
                        cont_values += 1
                    self.sql = self.sql[:-2] +") VALUES ("

                    for i in range(cont_values):
                        self.sql += "?,"

                    #if cont_values > 1:
                    self.sql = self.sql[:-1]

                    self.sql += ")"
                    #print("SQL:", self.sql)
                    #print("    ", self.datas_tuple)

                    self.executeSQL()
                else:
                    self.clear_attributes()
