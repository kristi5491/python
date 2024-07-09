## Magic methods. Task 3
***
#### Description

Implement class `Currency` and inherited classes `Euro`, `Dollar`, `Pound`.
Course is `1 EUR == 2 USD == 100 GBP`

You need to implement the following methods:

- `course` - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}
    
        >>> print(
            f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
            f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
            f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
        )
        Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
        Dollar.course(Pound) ==> 50.0 GBP for 1 USD
        Pound.course(Euro)   ==> 0.01 EUR for 1 GBP
 
- `to_currency` - method transforms currency from one currency to another. Method should return 
instance of a required currency.
    
        >>> e = Euro(100)
        >>> r = Pound(100)
        >>> d = Dollar(200)
        
        >>> print(
            f"e = {e}\n"
            f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
            f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
            f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
        )
        e = 100 EUR
        e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
        e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
        e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed
        
        >>> print(
            f"r = {r}\n"
            f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
            f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
            f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
        )
        r = 100 GBP
        r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
        r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
        r.to_currency(Pound) = 100.0 GBP  # Pound instance printed

- `+` - returns an instance of a new value

        >>> e = Euro(100)
        >>> r = Pound(100)
        >>> d = Dollar(200)
        >>> print(
            f"e + r  =>  {e + r}\n"
            f"r + d  =>  {r + d}\n"
            f"d + e  =>  {d + e}\n"
        )
        e + r  =>  101.0 EUR  # Euro instance printed
        r + d  =>  10100.0 GBP  # Pound instance printed
        d + e  =>  400.0 USD  # Dollar instance printed

- other comparison methods: `> < ==`

Please pay attention on examples. Your code should work exactly the same.
        

