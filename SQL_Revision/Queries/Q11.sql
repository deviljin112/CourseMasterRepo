use Northwind;

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