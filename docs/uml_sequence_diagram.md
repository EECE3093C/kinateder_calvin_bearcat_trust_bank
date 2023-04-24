# UML Sequence Diagram

This is a UML Sequence Diagram that illustrates the interactions between the classes `Bank`, `Account`, `SavingsAccount`, and `CheckingAccount` for creating accounts, depositing to a `CheckingAccount`, and withdrawing from a `SavingsAccount`.


```mermaid
sequenceDiagram
    participant Bank
    participant Account
    participant SavingsAccount
    participant CheckingAccount
    Bank->>SavingsAccount: create_account("SavingsAccount", 1, "Calvin", 500, 3.5)
    Bank->>CheckingAccount: create_account("CheckingAccount", 2, "Calvin", 100, 200)
    Account->>CheckingAccount: deposit(20)
    Account->>SavingsAccount: withdraw(40)
```