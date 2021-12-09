# Answers

## Coding (QUERY)

Feel free to see the raw .sql files in this folder for easy copy and paste into Azure to check against your queries. Also don't be hard on yourself if you didn't get it but instead take it as a good lesson and identifier for what areas you still need to work on! :) Happy coding!

### Question 1

Question 1 simply asks us to select the appropriate columns from table `Products`.

```sql
select
    ProductID,
    ProductName,
    UnitPrice,
    Discontinued
from Products
```

### Question 2

Question 2 asks for 3 seperate columns, each with an appropriate title i.e. "Max", "Min", "Average". Those are also the functions we have to use to select the appropriate values. Each column then contains requested values.

```sql
select
    MAX(UnitPrice) as 'Most Expensive',
    MIN(UnitPrice) as 'Cheapest',
    AVG(UnitPrice) as 'Average Price'
from Products
```

### Question 3

Question 3 similarly to Q1 asks for simple `SELECT` statement however we also need to add a condition in `WHERE` to specify that the price must be below £25.

```sql
select
    ProductID,
    ProductName,
    UnitPrice,
    Discontinued
from Products
where UnitPrice < 25
```

### Question 4

Question 4 requires `COUNT` to add up all the products that have been discontinued. No other field is required and the column should be named appropriately.

```sql
select
    count(*) as 'Quantity of Discontinued Products'
from Products
where Discontinued = 1
```

### Question 5

Question 5 requires a CASE implementation. There are 2 potential solutions here. We need a `CASE` when Discontinued is 1 (i.e. its dicontinued) and another when its 0 (still available). This can also be wrapped in a `WHERE THEN ELSE` where instead of stating `WHEN 0 THEN AVAILABLE` we could just do `ELSE AVAILABLE`. We also need to assign that column an appropriate name.

```sql
select
    ProductID,
    ProductName,
    UnitPrice,
    case
        when Discontinued = 1 then 'Discontinued'
        when Discontinued = 0 then 'Available'
        end as 'Discontinued'
from Products
```

### Question 6

Question 6 requires another form of `WHERE` clause, with checking a string argument. Many implementations are possible with `LIKE` and wildcards.

```sql
select
    CustomerID,
    CompanyName,
    ContactName,
    Phone,
    City
from Customers
where Country = 'UK'
```

### Question 7

Question 7 is the first question that requires a `JOIN`. We need to combine the `ORDERS` with `EMPLOYEES`. As orders contains the Primary Key of `EmployeeID`, we can use that information in a mutal table `Employees`. We can join both tables on that data, and then `SELECT` the first and last name. Second part of the question requires us to Concatinate the answer into one string then name the column appropriately. As we have already joined the tables together we will be able to see the concatinated name instead of `EmployeeID`. For the last part lets not forget the `WHERE` statement that includes only the results from the UK.

```sql
select
    Orders.OrderID,
    Orders.CustomerID,
    Employees.FirstName + ' ' + Employees.LastName as 'Employee Full Name',
    Orders.ShipCity
from Orders
inner join Employees on Orders.EmployeeID = Employees.EmployeeID
where Orders.ShipCountry = 'UK'
```

### Question 8

Similarly to Question 7, we are required to `INNER JOIN` on `CategoryID`. Same as before the Primary Key `CategoryID` is a mutual dataset used in both tables therefore we can easily link both tables together.

```sql
select
    Products.ProductID,
    Products.ProductName,
    Categories.CategoryName,
    Products.UnitPrice
from Products
inner join Categories on Products.CategoryID = Categories.CategoryID
```

### Question 9

Extending the previous 2 questions, in Question 9, we are required to `JOIN` 4 tables and concatinate employee's name. This question relies more on the being able to identify which data is mutual to which table and combining those keys. As there is no direct link between `Products` and `Orders` we cannot directly link the two tables. However, we have another table that is dependant on `Orders` that IS mutally linked with `Products` thats `Order Details`. By linking `Order Details` to `Orders` we are then able to link `Products` to `Order Details` and create a chain of links that ensure that we get the right data. Think of it as your house, you cannot enter your room from the front door, but the front door is linked to your door through lots of other doors in between. That chain of doors is the connection that we establishing here. (I hope this example is clear if you still dont understand please message me!)

```sql
select
    Orders.OrderID,
    Products.ProductName,
    Customers.CompanyName,
    Employees.FirstName + ' ' + Employees.LastName as 'Employee Full Name',
    Products.UnitPrice,
    [Order Details].[Quantity]
from Orders
inner join [Order Details] on Orders.OrderID = [Order Details].OrderID
inner join Products on [Order Details].ProductID = Products.ProductID
inner join Customers on Orders.CustomerID = Customers.CustomerID
inner join Employees on Orders.EmployeeID = Employees.EmployeeID
```

### Question 10

Question 10 is a mix of everything from previous questions, with an added challenge of getting the age of employees which we have done in a lesson. Similarly to before, we dont have a direct link from `Categories` to `Orders` but we do have a link to `Products` which is linked to `Order Details` which is linked to `Orders`. Creating a long link of data. As for employee age its the `DATEDIFF` function that returns the difference between the two years specified. If we wanted to be "extra" correct we could concatinate seperate variables, such as "YEAR", "MONTH", "DAY" and check the true age of each employee. However, this would never be expected in an SQL exam nor anyone coding it so we don't need to worry about it :).

```sql
select
    Orders.OrderID,
    Products.ProductName,
    Categories.CategoryName,
    Customers.CompanyName,
    Employees.FirstName + ' ' + Employees.LastName as 'Employee Full Name',
    DATEDIFF(yy, Employees.BirthDate, GETDATE()) as 'Employee Age',
    Products.UnitPrice,
    [Order Details].[Quantity],
    case
        when Orders.ShippedDate - Orders.RequiredDate > 0 then 'LATE'
        else 'ON TIME'
        end
        as 'Shipping Time'

from Orders
inner join [Order Details] on Orders.OrderID = [Order Details].OrderID
inner join Products on [Order Details].ProductID = Products.ProductID
inner join Customers on Orders.CustomerID = Customers.CustomerID
inner join Employees on Orders.EmployeeID = Employees.EmployeeID
inner join Categories on Products.CategoryID = Categories.CategoryID
```

### Question 11

Last question which I personally think is the hardest to grasp. It may not be as hard as the previous ones in terms of how much needs to be coded, however its the hardest to fully master. In this question we need to use aggregate functions. As the lecture explains these require `HAVING` which i didnt include in this question as I thought it was already hard enough. Because aggregate functions create one single field of data from the set they are given, we need to "combine" all that remaining data into one row. In other words, when we `COUNT` all the orders we are essentially combining all of the `OrderID` into one single digit, which is the total amount of values in that column. However when we use `COUNT` it does not combine all of the other arguments in `SELECT`. This is where `GROUP BY` comes in. We need to manually combine all the duplications into one row. Since we have just a single digit for (this is an example) "Hubert's Finest Dining" orders, but the name "Hubert's Finest Dining" still occurs let's say 20 times in the list. We therefore group it into one occurance that is put together with the `COUNT`. As for the `Total Spent` part of the question. We had to use `SUM` in which we times `UnitPrice` with `Quantity` to get the total amount of money spent by a company. Lastly, we needed to sort the data from highest to lowest with `ORDER BY` our created column, and select the `TOP 5` values in `SELECT` statement. This required (in my opinion) all of the hardest concepts to fully grasp into one question. Pat yourself on the back if you managed to get it! And if you didn't that's okey! I highly doubt this level of a quesiton would be in an exam :) but feel free to message me to explain it even further.

```sql
select top 5
    Customers.CustomerID,
    Customers.CompanyName,
    COUNT(Orders.OrderID) as 'Order Count',
    SUM([Order Details].UnitPrice * [Order Details].Quantity) as 'Total Spent'
from orders
inner join Customers on Orders.CustomerID = Customers.CustomerID
inner join [Order Details] on Orders.OrderID = [Order Details].OrderID
group by
    Customers.CustomerID,
    Customers.CompanyName
order by 'Total Spent' DESC
```
