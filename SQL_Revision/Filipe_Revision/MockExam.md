# SQL Practical Exercise

## Exercise 1

Question 1

```sql
select
    CustomerID,
    CompanyName,
    Address,
    City,
    Region,
    PostalCode,
    Country
from Customers
where City = 'Paris' or City = 'London'
```

Question 2

```sql
select *
from Products
where QuantityPerUnit like '%bottle%'
```

Question 3

```sql
select
    Products.*,
    Suppliers.CompanyName,
    Suppliers.Country
from Products
inner join Suppliers on Products.SupplierID = Suppliers.SupplierID
where QuantityPerUnit like '%bottle%'
```

Question 4

```sql
select
    count(Products.ProductID) as 'Quantity',
    CategoryName
from Products
inner join Categories on Products.CategoryID = Categories.CategoryID
group by CategoryName
order by 'Quantity' DESC
```

Question 5

```sql
select
    TitleOfCourtesy + ' ' + FirstName + ' ' + LastName as 'Full Name',
    City
from Employees
where Country = 'UK'
```

Question 6

```sql
select
    Territories.RegionID,
    format(sum([Order Details].Quantity * [Order Details].UnitPrice), '###,###,###') as 'Sales Total'
from Territories
inner join EmployeeTerritories on Territories.TerritoryID = EmployeeTerritories.TerritoryID
inner join Employees on EmployeeTerritories.EmployeeID = Employees.EmployeeID
inner join Orders on Employees.EmployeeID = Orders.EmployeeID
inner join [Order Details] on Orders.OrderID = [Order Details].OrderID
group by Territories.RegionID
having sum([Order Details].Quantity * [Order Details].UnitPrice) > 1000000
```

Question 7

```sql
select *
from Orders
where Freight > 100 and (ShipCountry = 'UK' or ShipCountry = 'USA')
```

Question 8

```sql
select
    OrderID,
    Discount
from [Order Details]
where Discount =
    (select MAX(Discount)
    from [Order Details])
```
