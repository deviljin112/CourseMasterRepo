# Questions from Filipe's presentation

## First part

Using a Subquery in the WHERE clause, list all Orders (Order ID, Product ID, Unit Price, Quantity and Discount) from the [Order Details] table where the product has been discontinued​.

```sql
select
    OrderID,
    ProductID,
    UnitPrice,
    Quantity,
    Discount
from [Order Details]
where ProductID not in
(
    select ProductID
    from Products
    where Discontinued = 0
)
```

## Second part

​Now repeat the same exercise using a simple join​

```sql
select
    OrderID,
    OD.ProductID,
    OD.UnitPrice,
    Quantity,
    Discount
from [Order Details] as OD
inner join Products on OD.ProductID = Products.ProductID
where Products.Discontinued != 0
```

## Last Slide (union all)

Try making an outer join!

- This fucking question is the most useless example of UNION that I've ever seen...

```sql
select
    EmployeeID,
    FirstName
from Employees
UNION ALL
select
    ProductID,
    ProductName
from Products
```
