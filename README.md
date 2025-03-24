![Python versions](https://img.shields.io/pypi/pyversions/migropy?style=flat-square&logo=python&logoColor=white&color)
![Test](https://img.shields.io/github/actions/workflow/status/fredimatteo/migratron/test.yml?style=flat-square&logo=github&logoColor=white&color&label=Test)

# 🛠️ Migropy

**Migropy** is a lightweight and extensible Python library for managing **database migrations**.  
Designed for simplicity and flexibility, it helps teams apply, track, and version-control schema changes across multiple
environments.

---

## 🚀 Features

- ✅ Versioned migrations with up/down support
- ✅ Compatible with PostgreSQL & MySQL
- ✅ CLI for common migration operations
- ✅ Safe and idempotent execution
- ✅ Customizable migration directory structure

---

## 📦 Installation

```bash
pip install migropy
```

---

## 📖 How to use - CLI

### 1. Initialize a new migration project

This command will create a new directory called `migrations` with the necessary files to manage your migrations & db
parameters.
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
type = postgres # or mysql

[logger]
level = DEBUG
```

### 4. Create a new migration

This command will create a new migration file in the `migrations` directory with the following template:

```sql
-- Up migration

-- Down migration
```

```bash
migropy generate 'migration name'
```

### 5. Apply the migrations

This command will apply all the migrations in the `migrations` directory. Please note the migrations are applied in
the prefix order.
```bash
migropy upgrade
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

## 🧪 Running Unit Tests

To run the unit tests using poetry, you can use the following command:

```bash
poetry run pytest --rootdir=tests
```

---

## 📝 Changelog

See the full [CHANGELOG.md](https://github.com/fredimatteo/migratron/blob/main/CHANGELOG.md)

### Latest Changes

- **0.2.1** – Increase minimum python version to 3.10 & refactor MigrationEngine
- **0.2.0** – MySQL database support
- **0.1.1** – Initial project setup with PostgreSQL

---

## 📄 License

MIT License © 2025 — teoxy
