# 🛠️ Migropy

**Migropy** is a lightweight and extensible Python library for managing **database migrations**.  
Designed for simplicity and flexibility, it helps teams apply, track, and version-control schema changes across multiple
environments.

---

## 🚀 Features

- ✅ Versioned migrations with up/down support
- ✅ Compatible with PostgreSQL
- ✅ CLI for common migration operations
- ✅ Safe and idempotent execution
- ✅ Customizable migration directory structure

---

## 📦 Installation

```bash
pip install migropy
```

---

## 📖 How to use

### 1. Initialize a new migration project

```bash
migropy init
```

### 2. Go to the migrations directory

```bash
cd migrations
```

### 3. Fill the config.ini file

```ini
[database]
host = localhost
port = 5432
user = postgres
password = postgres
dbname = my_database
type = postgres

[logger]
level = DEBUG
```

### 4. Create a new migration

```bash
migropy generate 'migration name'
```

### 5. Apply the migrations

```bash
migropy apply
```

---

## 📄 Migration example

```sql
-- Up migration
CREATE TABLE users
(
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Down migration
DROP TABLE users;
```

---

## ⚙️ Available commands

| Comando                   | Descrizione                   |
|---------------------------|-------------------------------|
| `migropy init`            | Init migratron environment    |
| `migropy generate <name>` | Generate a new sql migration  |
| `migropy upgrade`         | Apply all the migration       |
| `migropy downgrade`       | Rollback all revisions        |
| `migropy list `           | Show current migration status |

---

## 📄 License

MIT License © 2025 — teoxy
