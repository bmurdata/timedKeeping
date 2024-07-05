import sqlite3
con = sqlite3.connect("dev.db")


qry='''
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Balances;
DROP TABLE IF EXISTS Balance_Transactions;
DROP TABLE IF EXISTS Jobs;

CREATE TABLE IF NOT EXISTS Employees (
    EmplID INTEGER PRIMARY KEY,
    Fname TEXT NOT NULL,
    Lname TEXT NOT NULL,
    Hired DATE NOT NULL,
    Title TEXT NOT NULL,
    WorkerType TEXT NOT NULL,
    Status TEXT NOT NULL,
    JobNum INTEGER NOT NULL,
    Department TEXT NOT NULL,
    BusinessTitle TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Balances (
    code TEXT PRIMARY KEY,
    Amount REAL NOT NULL,
    Type TEXT NOT NULL,
    emplID INTEGER NOT NULL,
    FOREIGN KEY (emplID) REFERENCES Employees (EmplID)
);
CREATE TABLE Balance_Transactions (
    Amount REAL NOT NULL,
    Type TEXT NOT NULL,
    Reason TEXT NOT NULL,
    emplID INTEGER NOT NULL,
    balanceCode TEXT NOT NULL,
    dateEffective DATE NOT NULL,
    dateCreated DATE NOT NULL,
    FOREIGN KEY (emplID) REFERENCES Employees (EmplID),
    FOREIGN KEY (balanceCode) REFERENCES Balances (code)
);
CREATE TABLE IF NOT EXISTS Jobs (
    JobNum INTEGER PRIMARY KEY,
    EligibleTitles TEXT NOT NULL,
    Location TEXT NOT NULL,
    JobType TEXT NOT NULL,
    AssignedBy TEXT NOT NULL,
    Flag TEXT NOT NULL
);


'''
con.execute(qry)
