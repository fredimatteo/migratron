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

This command will create a new directory called `migropy` with the necessary files to manage your migrations & db
parameters.
```bash
migropy init
```

### 2. Go to the migrations directory

```bash
cd migropy
```

### 3. Fill the config.ini file

```ini
[database]
# database connection parameters
# available types: postgres, mysql
host = localhost
port = 5432
user = postgres
password = postgres
dbname = my_database
type = postgres # or mysql

[migrations]
# path to migration scripts
# use forward slashes (/) also on windows to provide an os agnostic path
script_location = migropy

[logger]
# available levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
level = DEBUG
```

### 4. Create a new migration

This command will create a new migration file in the `migropy/versions` directory with the following template:

```bash
migropy generate 'migration name'
```

```sql
-- Up migration

-- Down migration
```

### 5. Apply the migrations

This command will apply all the migrations in the `migrations` directory. Please note the migrations are applied in
the prefix order.
```bash
migropy upgrade
```

---

## 🐍 How to use - Python

You can also use **Migropy** as a library in your Python code. Here is an example of how to use it:

```python
# Importing the function to load the migration configuration
from migropy.configuration_parser import load_config

# Importing the Postgres database adapter
from migropy.databases.postgres import Postgres

# Importing the common database configuration structure
from migropy.databases.commons import DbConfig

# Importing the migration engine responsible for applying migrations
from migropy.migration_engine import MigrationEngine

# Create a database configuration object with connection parameters
db_config = DbConfig(
    host="localhost",      # Database server hostname or IP
    port=5432,             # Default PostgreSQL port
    user="user",           # Username to connect to the database
    password="password",   # Password for the given user
    database="test"        # Name of the target database
)

# Instantiate a Postgres database connection using the provided configuration
db = Postgres(db_config)

# Create a MigrationEngine instance with:
# - the database connection
# - the loaded configuration (usually from a file like migropy.ini)
engine = MigrationEngine(db=db, config=load_config())

# Initialize the migropy environment and create the necessary tables
# use it just once!!!
engine.init()

# Generate a new migration revision with a descriptive name
engine.generate_revision(revision_name='first revision')

# Apply all pending migrations to upgrade the database schema
engine.upgrade()

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

## 🤝 Contributing

We welcome contributions!  
To get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a pull request 🚀

---

## 📫 Support

For issues, feature requests or general questions, open an issue on [GitHub Issues](https://github.com/fredimatteo/migratron/issues).


---

## 📄 License

MIT License © 2025 — teoxy
