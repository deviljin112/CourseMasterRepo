# SQL Queering Homework

Use your SQL sever to run the queries and come to an answer.
Pay attention to detail, as there is ONE right answer and following guidelines & or instructions is an important skill for consultants.

Note we will refer to Northwind Database as NWDB
Please read on.

**Important**
Your response should always be the **SQL query** + the short answer where appropriate.

## Queries

### Q1 - How many orders in NWDB

- Query:

```sql
select count(OrderID) from Orders;
```

- Response:
- 830

### Q2 - How many order that the Ship City is Rio de Janeiro

- Query:

```sql
select count(OrderID) from Orders where ShipCity = 'Rio de Janeiro';
```

- Response:
- 34

### Q3 - Select all orders that the Ship City is Rio de Janeiro or Reims

- Query:

```sql
select count(OrderID) from Orders where ShipCity in ('Rio de Janeiro', 'Reims');
```

- Response:
- [Json Output](Q3.json)

### Q4 - Select all of the entries where the Company name has a z or a Z in the table of Customers

- Query:

```sql
select count(CustomerID) from Customers where CompanyName like '%z%' or CompanyName like '%Z%';
```

- Response:
- [Json Output](Q4.json)

### Q5 - We need to update all of our FAX information! This Day and age it is a must! Find me the Name of All of the companies that we do not have their FAX numbers! I would also like to know with whom I need to speak with, their contact numbers and what city they are base in

- Query:

```sql
select CompanyName, ContactName, Phone, City, Fax from Suppliers where Fax is null;
```

- Response:
- [Json Output](Q5.json)

### Q6 - Ahh there you are! My prize SPARTANTS! MY MARES AND MY STALLIONS! We need to re-target all of our Customers in Paris! Get me information on these clients

- Query:

```sql
select * from Customers where City = 'Paris';
```

- Response:
- [Json Output](Q6.json)

### Q7 - WAIT! Where are you going? (...) These clients are hard to sell too! We need more intel.. Can you find out, from these clients from Paris, whom orders the most by quantity? Who are our top 5 clients

- Query:

```sql
select top 5 count(Orders.OrderID) as 'Quantity of Orders', Customers.CompanyName
from Customers
left join Orders on Customers.CustomerID = Orders.CustomerID
where Customers.City = 'Paris'
group by Customers.CompanyName
order by count(Orders.OrderID) DESC;
```

- Response:
- [Json Output](Q7.json)

### Q8 - OMG What are you? Some kind of SQL Guardian Angel? THIS IS AMAZING! May God pay you handsomely because I have no cash on me!..  I do have one more request. I need to know more about these these Paris client. Can you find out which ones their deliveries took longer than 10 days? Display the Business/client name, contact name, all their contact details (don't forget the fax!), as well as the number of deliveries that where overdue! Just add a column named: 'Number overdue orders'! simple, thank you

- Query (without Paris as argument):

```sql
select top 5
    Customers.CustomerID,
    Customers.CompanyName,
    Customers.ContactName,
    Customers.Phone,
    Customers.Fax,
    count(Orders.OrderID) as 'Overdue Orders'
from Customers
inner join Orders on Customers.CustomerID = Orders.CustomerID
where Orders.ShippedDate - Orders.RequiredDate > 10
group by
    Customers.CustomerID,
    Customers.CompanyName,
    Customers.ContactName,
    Customers.Phone,
    Customers.Fax
order by count(Orders.OrderID) DESC;
```

- Response:
- [Json Output](Q8.json)

- Query (with Paris as argument):

```sql
select top 5
    Customers.CustomerID,
    Customers.CompanyName,
    Customers.ContactName,
    Customers.Phone,
    Customers.Fax,
    count(Orders.OrderID) as 'Overdue Orders'
from Customers
inner join Orders on Customers.CustomerID = Orders.CustomerID
where Orders.ShippedDate - Orders.RequiredDate > 10 and City = 'Paris'
group by
    Customers.CustomerID,
    Customers.CompanyName,
    Customers.ContactName,
    Customers.Phone,
    Customers.Fax
order by count(Orders.OrderID) DESC;
```

- Response:
- None
