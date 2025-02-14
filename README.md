# Test
Test
-- For SQL Server:
SELECT 
    t.name AS table_name,
    i.name AS primary_key_name,
    COL_NAME(ic.object_id, ic.column_id) AS column_name
FROM 
    sys.tables AS t
JOIN 
    sys.indexes AS i 
ON 
    t.object_id = i.object_id
JOIN 
    sys.index_columns AS ic 
ON 
    i.object_id = ic.object_id AND i.index_id = ic.index_id
WHERE 
    i.is_primary_key = 1
    AND t.name = 'your_table_name';
