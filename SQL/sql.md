# SQL Learning Roadmap

## 1. **Basic SQL Syntax**
### **SQL Keywords**
- Reserved words in SQL like `SELECT`, `INSERT`, `DELETE`, `UPDATE`, etc.

### **Data Types**
- Integer (`INT`, `BIGINT`), String (`VARCHAR`, `TEXT`), Date/Time (`DATE`, `TIMESTAMP`), etc.

### **Operators**
- Arithmetic (`+`, `-`, `*`, `/`)
- Comparison (`=`, `>`, `<`, `!=`)
- Logical (`AND`, `OR`, `NOT`)

### **SQL Statements**
#### **SELECT (Retrieving Data)**
```sql
SELECT name, age FROM students WHERE age > 18;
```
**Input Table:**
| id | name  | age |
|----|-------|-----|
| 1  | Alice | 20  |
| 2  | Bob   | 17  |
| 3  | John  | 22  |

**Output:**
| name  | age |
|-------|-----|
| Alice | 20  |
| John  | 22  |

---

## 2. **Data Definition Language (DDL)**
#### **CREATE TABLE (Defining Structure)**
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);
```

#### **ALTER TABLE (Modifying Structure)**
```sql
ALTER TABLE employees ADD COLUMN department VARCHAR(50);
```

#### **DROP TABLE (Deleting Structure)**
```sql
DROP TABLE employees;
```

#### **TRUNCATE TABLE (Remove Data)**
```sql
TRUNCATE TABLE employees;
```

---

## 3. **Data Manipulation Language (DML)**
#### **INSERT (Adding Data)**
```sql
INSERT INTO employees (id, name, salary) VALUES (1, 'Alice', 50000);
```

#### **UPDATE (Modifying Data)**
```sql
UPDATE employees SET salary = 55000 WHERE id = 1;
```

#### **DELETE (Removing Data)**
```sql
DELETE FROM employees WHERE id = 1;
```

#### **ORDER BY (Sorting Data)**
```sql
SELECT name, salary FROM employees ORDER BY salary DESC;
```

#### **GROUP BY & HAVING (Aggregations)**
```sql
SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 60000;
```

---

## 4. **Joins**
#### **INNER JOIN (Matching Records in Both Tables)**
```sql
SELECT employees.name, department.name FROM employees
JOIN department ON employees.department_id = department.id;
```

#### **LEFT JOIN (All Records from Left, Matching from Right)**
```sql
SELECT employees.name, department.name FROM employees
LEFT JOIN department ON employees.department_id = department.id;
```

#### **RIGHT JOIN (All Records from Right, Matching from Left)**
```sql
SELECT employees.name, department.name FROM employees
RIGHT JOIN department ON employees.department_id = department.id;
```

#### **FULL OUTER JOIN (All Records from Both Tables)**
```sql
SELECT employees.name, department.name FROM employees
FULL OUTER JOIN department ON employees.department_id = department.id;
```

---

## 5. **Subqueries**
#### **Nested Subquery Example**
```sql
SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

## 6. **Advanced SQL Functions**
### **String Functions**
#### **CONCAT (Merging Strings)**
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
```

#### **LENGTH (String Length)**
```sql
SELECT LENGTH(name) FROM employees;
```

### **Date and Time Functions**
#### **DATEADD (Add Time to a Date)**
```sql
SELECT DATEADD(DAY, 7, GETDATE());
```

### **Numeric Functions**
#### **ROUND (Rounding Numbers)**
```sql
SELECT ROUND(salary, 2) FROM employees;
```

---

## 7. **Indexes**
#### **Creating an Index**
```sql
CREATE INDEX idx_salary ON employees (salary);
```

---

## 8. **Transactions**
#### **ACID Properties**
- **Atomicity**: All or nothing
- **Consistency**: Maintains database integrity
- **Isolation**: Transactions do not interfere
- **Durability**: Changes persist after commit

#### **Transaction Example**
```sql
BEGIN TRANSACTION;
UPDATE employees SET salary = salary + 5000 WHERE id = 1;
COMMIT;
```

---

## 9. **Stored Procedures & Functions**
#### **Creating a Stored Procedure**
```sql
CREATE PROCEDURE GetEmployeeSalary @id INT AS
BEGIN
    SELECT salary FROM employees WHERE id = @id;
END;
```

---

## 10. **Performance Optimization**
#### **Query Optimization Techniques**
- Use **indexes** to speed up searches.
- Optimize **joins** by indexing foreign keys.
- Avoid unnecessary **subqueries**.

---

## 11. **Advanced SQL Concepts**
#### **Recursive Queries (CTEs)**
```sql
WITH EmployeeHierarchy AS (
    SELECT id, name, manager_id FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id FROM employees e
    JOIN EmployeeHierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM EmployeeHierarchy;
```

#### **Window Functions (Ranking)**
```sql
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
       RANK() OVER (ORDER BY salary DESC) AS rank_num,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank_num,
       LEAD(salary) OVER (ORDER BY salary DESC) AS next_salary,
       LAG(salary) OVER (ORDER BY salary DESC) AS previous_salary
FROM employees;
```

#### **Dynamic SQL**
```sql
DECLARE @sql NVARCHAR(MAX);
SET @sql = 'SELECT * FROM employees WHERE salary > 50000';
EXEC sp_executesql @sql;
```

#### **Pivot & Unpivot Operations**
- **Pivot**: Converts rows into columns.
- **Unpivot**: Converts columns into rows.

---

## Conclusion
This roadmap provides a structured learning path for mastering SQL. Start with the basics and gradually move towards advanced concepts. Happy Learning!

