from get_path import GetPath
from db_sqlite import DatabaseManager

gp = GetPath()

db_name = 'teste.db'
fields = []

db_con = DatabaseManager()
db_con.connect(gp.get_path() +f"/{db_name}")

#print(db_con)

# Create 'Person' entity without arguments ============================================
db_con.create_table('Person')

# Add columns on 'Person' entity ------------------------------------------------------

field_1 = {
    'name':'name',
    'type':'Varchar',               # String (i.e: 'Varchar')
    'argument':'(100)',             # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': False,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}
fields.append(field_1)

field_2 = {
    'name':'born_date',
    'type':'DATE',                  # String (i.e: 'Varchar')
    'argument':'',                  # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': False,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}

fields.append(field_2)

db_con.add_column('Person', fields)


fields.clear()


# Create 'PersonAddress' entity with arguments ========================================
field_0 = {
    'name':'cod_person',
    'type':'INTEGER',               # String (i.e: 'Varchar')
    'argument':'',                  # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': False,
    'is_foreignkey': True,
    'reference_table': 'Person',    # <table_name>
    'reference_table_field': 'id',  #(id)
}
fields.append(field_0)

field_1 = {
    'name':'address',
    'type':'Varchar',               # String (i.e: 'Varchar')
    'argument':'(150)',             # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': True,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}
fields.append(field_1)

field_2 = {
    'name':'number',
    'type':'INTEGER',               # String (i.e: 'Varchar')
    'argument':'',                  # String (i.e: '(100)')
    'default_value': '0',           # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': True,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}
fields.append(field_2)

field_3 = {
    'name':'distric',
    'type':'Varchar',               # String (i.e: 'Varchar')
    'argument':'(150)',             # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': False,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}
fields.append(field_3)

field_4 = {
    'name':'city',
    'type':'Varchar',               # String (i.e: 'Varchar')
    'argument':'(150)',             # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': False,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}
fields.append(field_4)

field_5 = {
    'name':'uf',
    'type':'Varchar',               # String (i.e: 'Varchar')
    'argument':'(2)',               # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'unique': False,
    'not_null': False,
    'is_foreignkey': False,
    'reference_table': None,        # <table_name>
    'reference_table_field': None,  #(id)
}
fields.append(field_5)

db_con.create_table('PersonAddress', fields=fields)


fields.clear()


# Create 'Schooling' entity with arguments ===========================================
field_1 = {
    'name':'name',
    'type':'Varchar',               # String (i.e: 'Varchar')
    'argument':'(150)',             # String (i.e: '(100)')
}
fields.append(field_1)

db_con.create_table('Schooling', fields=fields)


fields.clear()

# Insert values in 'Schooling' entity -------------------------------------------------
values = []
values.append({'name': 'Educação Infantil'})
values.append({'name': 'Ensino Fundamental I'})
values.append({'name': 'Ensino Fundamental I'})
values.append({'name': 'Ensino Médio'})
values.append({'name': 'Ensino Médico com Técnico'})
values.append({'name': 'Graduação'})
values.append({'name': 'Pós-graduação'})
values.append({'name': 'Mestrado'})
values.append({'name': 'Doutorado'})

db_con.insert_values('Schooling', values)


fields.clear()
# Add FK column on 'Person' entity ====================================================

field_1 = {
    'name':'cod_schooling',
    'type':'INTEGER',               # String (i.e: 'Varchar')
    'argument':'',                  # String (i.e: '(100)')
    'default_value': '',            # String (i.e: 'Jhon Doe')
    'is_foreignkey': True,
    'reference_table': 'Schooling', # <table_name>
    'reference_table_field': 'id',  #(id)
}
fields.append(field_1)

db_con.add_column('Person', fields=fields)

# =====================================================================================


