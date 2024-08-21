import sqlite3

class TransactionObject:
    def __init__(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cur = self.conn.cursor()

    def execute(self, sql, parms=None):
        if parms is None:
            self.cur.execute(sql)
        else:
            self.cur.execute(sql, parms)
        return True

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

def initDB():
    trans = TransactionObject()
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.close()

def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.close()

def view():
    trans = TransactionObject()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.close()
    return rows

def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObject()
    trans.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
    rows = trans.fetchall()
    trans.close()
    return rows

def delete(id):
    trans = TransactionObject()
    trans.execute("DELETE FROM clientes WHERE id=?", (id,))
    trans.persist()
    trans.close()

def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
    trans.persist()
    trans.close()

# Inicializa o banco de dados
initDB()
