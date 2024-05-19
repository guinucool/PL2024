# Gramática independete de contexto para operações numéricas
**Autor: Guilherme Oliveira, A100592**

## Gramática
```
T = {'?', '!', '=', ID, NUMBER, '+', '-', '*', '/', '^', '(', ')'}

N = {S, Instruction, Expression, ExpOperator, Product, ProOperator, Factor, FacOperator, Term}

S = S

P = {
    S : Instruction S                       (LA = {'?', '!', ID})
      | $                                   (LA = {$})

    Instruction : '?' ID                    (LA = {'?'})
                | '!' Expression            (LA = {'!'})
                | ID '=' Expression         (LA = {ID})

    Expression : Product ExpOperator        (LA = {'(', '+', '-', ID, NUMBER})
    
    ExpOperator : '+' Expression            (LA = {'+'})
                | '-' Expression            (LA = {'-'})
                | $                         (LA = {$, ')'})

    Product : Factor ProOperator            (LA = {'(', '+', '-', ID, NUMBER})

    ProOperator : '*' Product               (LA = {'*'})
                | '/' Product               (LA = {'/'})
                | $                         (LA = {$, '+', '-', ')'})

    Factor : Term FacOperator               (LA = {'(', '+', '-', ID, NUMBER})

    FacOperator : '^' Factor                (LA = {'^'})
                | $                         (LA = {$, '+', '-', '*', '/', ')'})

    Term : '(' Expression ')'               (LA = {'('})
         | '+' Term                         (LA = {'+'})
         | '-' Term                         (LA = {'-'})
         | ID                               (LA = {ID})
         | NUMBER                           (LA = {NUMBER})
}
```