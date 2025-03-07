import sqlite3
from search.metizes.schemas import MetizCreate
# import pandas as pd


def create_table_metizes() -> None:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Metizes(
    id INTEGER PRIMARY KEY,
    number_in_catalog TEXT NULL,
    number_in_catalog_agb TEXT NULL,
    name_in_catalog TEXT NULL,
    name_in_kd TEXT NULL,
    name_in_catalog_agb TEXT NULL,
    standard TEXT NULL,
    type TEXT NULL,
    profile TEXT NULL,
    diameter_nominal TEXT NULL,
    step TEXT NULL,
    length TEXT NULL,
    accuracy TEXT NULL,
    material_or_coverage TEXT NULL,
    assigned TEXT NULL,
    note TEXT NULL,
    applicability TEXT NULL,
    date TEXT NULL)""")
    connection.commit()
    connection.close()


def create_new_item(item: MetizCreate) -> None:
    print(item.number_in_catalog_agb)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Metizes (
        number_in_catalog,
        number_in_catalog_agb,
        name_in_catalog,
        name_in_kd,
        name_in_catalog_agb,
        standard,
        type,
        profile,
        diameter_nominal,
        step,
        length,
        accuracy,
        material_or_coverage,
        assigned,
        note,
        applicability,
        date        
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
        item.number_in_catalog,
        item.number_in_catalog_agb,
        item.name_in_catalog,
        item.name_in_kd,
        item.name_in_catalog_agb,
        item.standard,
        item.type,
        item.profile,
        item.diameter_nominal,
        item.step,
        item.length,
        item.accuracy,
        item.material_or_coverage,
        item.assigned,
        item.note,
        item.applicability,
        item.date))
    connection.commit()
    connection.close()


def search_all_items():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Metizes")
    items = cursor.fetchall()
    connection.commit()
    connection.close()
    return items


def search_item_by_index(item_id: int):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM Metizes
        WHERE id = ?
        """, (item_id,))
    result = cursor.fetchall()
    connection.close()
    return result


def search_item_by_request(request: str):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    result_search = set()
    request = "%" + request + '%'
    for elem in (
            "number_in_catalog", "number_in_catalog_agb", "name_in_catalog", "name_in_kd", "name_in_catalog_agb",
            "standard", "type", "profile", "diameter_nominal", "step", "length", "accuracy", "material_or_coverage",
            "assigned", "note", "applicability", "date"):
        cursor.execute(f"""
    SELECT * FROM Metizes
    WHERE LOWER({elem}) LIKE LOWER(?);
    """, (request,))
        result = cursor.fetchall()
        for res in result:
            result_search.add(res)
    connection.close()
    # for elem in result_search:
    #     print(elem)
    return result_search


def update_item(item_id: int, key1: str, value1: str):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f"""
        UPDATE Metizes SET {key1} = ? WHERE id = ?
        """, (value1, item_id))
    connection.commit()
    connection.close()


def delete_item(item_id: int):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""
            DELETE FROM Metizes WHERE id = ?
            """, (item_id,))
    connection.commit()
    connection.close()


# new_item = MetizCreate(
#     number_in_catalog='234',
#     number_in_catalog_agb='56347',
#     name_in_catalog='56857',
#     name_in_kd='5858',
#     name_in_catalog_agb='56858',
#     standard='565589',
#     type='7070',
#     profile='7089789',
#     diameter_nominal='07897897',
#     step='Бодрыйwertwet',
#     length='70879',
#     accuracy='078978',
#     material_or_coverage='7089789',
#     assigned='177078978978',
#     note='1789789789',
#     applicability='178978978344',
#     date='1278978978'
# )

def assert_data():
    df = pd.read_excel('data_test.xlsx')
    result_list = []
    for _, row in df.iterrows():
        processed_row = []
        for column in df.columns:
            value = row[column]
            if value is None or pd.isna(value):
                processed_row.append('-')
            else:
                processed_row.append(str(value))
        result_list.append(processed_row)
    for item in result_list:
        result_item = MetizCreate(
            number_in_catalog=item[0],
            number_in_catalog_agb=item[1],
            name_in_catalog=item[2],
            name_in_kd=item[3],
            name_in_catalog_agb=item[4],
            standard=item[5],
            type=item[6],
            profile=item[7],
            diameter_nominal=item[8],
            step=item[9],
            length=item[10],
            accuracy=item[11],
            material_or_coverage=item[12],
            assigned=item[13],
            note=item[14],
            applicability=item[15],
            date=item[16])
        create_new_item(result_item)

    # for item in items_list:
    #     if item:
    #         result_item = MetizCreate(
    #         number_in_catalog=item[0],
    #         number_in_catalog_agb=item[1],
    #         name_in_catalog=item[2],
    #         name_in_kd=item[3],
    #         name_in_catalog_agb=item[4],
    #         standard=item[5],
    #         type=item[6],
    #         profile=item[7],
    #         diameter_nominal=item[8],
    #         step=item[9],
    #         length=item[10],
    #         accuracy=item[11],
    #         material_or_coverage=item[12],
    #         assigned=item[13],
    #         note=item[14],
    #         applicability=item[15],
    #         date=item[16])
    #         create_new_item(result_item)
