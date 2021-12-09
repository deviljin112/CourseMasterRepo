# D3v & Farah Revision Session

## Coding (QUERY)

Attempt as many or as little as you want or feel like! The questions are in what I would consider correct difficulty but each person learns at different rates and probably finds different subjects harder or easier, so dont be discouraged by the difficulty if you cant do Easy but find "Hard" easier. It's just how I would label each of those tasks. If you don't understand a question, ask me or Farah to explain!

- Here's a small list of resources that may help you answering the queries:
  - [w3school](https://www.w3schools.com/sql/)
  - [SQL Join Types](https://www.sqlservertutorial.net/sql-server-basics/sql-server-joins/)
  - [w3school Join](https://www.w3schools.com/sql/sql_join.asp)
  - [CASE statement](https://www.sqlshack.com/understanding-sql-server-case-statement/)
  - [GROUP BY and ORDER BY](https://www.sqlservertutorial.net/sql-server-basics/sql-server-group-by/)

### Question 1 - Easy

- Write a Query to get ProductID, ProductName, UnitPrice and Discontinued.
- TIP: For this question you need `Products` table.

### Question 2 - Easy

- What is the most expensive, cheapest, and average price of products?
- TIP: For this question you need `Products` table.
- Explanation: Each Column should be have a name appropriate for the value, and there should be only one row containing prices.

### Question 3 - Intermediate

- Write a Query that get ProductID, ProductName, UnitPrice and Discontinued, only of products that are less than £25.
- TIP: For this question you need `Products` table.

### Question 4 - Intermediate

- Write a query that counts all discontinued products.
- TIP: For this question you need `Products` table.

### Question 5 - Advanced

- Write a Query to get ProductID, ProductName, UnitPrice and Discontinued but instead of `0` or `1`, writes `Discontinued` or `Available` in a new column.
- TIP: For this question you need `Products` table.

### Question 6 - Advanced

- Write a Query to list all Customers from the `UK`. Query should include CustomerID, CompanyName, ContactName, Phone and City.
- TIP: For this question you need `Customers` table.

### Question 7 - Hard

- Write a Query that shows all Orders that were Shipped to the `UK`. Query should include OrderID, CustomerID, Employee's Full Name and ShipCity.
- TIP: For this question you need both `Employees` and `Orders` table.

### Question 8 - Harder

- Write a Query that shows ProductID, ProductName, CategoryName and UnitPrice.
- TIP: For this question you need both `Products` and `Categories` table.

### Question 9 - Godlike

- Write a Query that shows OrderID, ProductName, CompanyName, Employee's Full Name, UnitPrice, Quantity Purchased as well as ShipCountry.
- TIP: For this question you need `Orders`, `Order Details`, `Products`, `Employees` and `Customers` table.

### Question 10 - Ultimate God Skillz

- Write a Query that extends from last question by adding CategoryName, Employee's Age, and a new column stating whether the shipping was `LATE` or `ON TIME` called `Shipping Time`.
- TIP: For this question you need all previous tables but also `Categories`.

### Question 11 - 360* No Scope Try Hard Impossible Challenge 420

- Write a Query that groups all Customers by CustomerID and CompanyName then display how many orders they have made so far. Followed by how much they have spent on all orders. Then show only the top 5 customers from most spent money to least.
- TIP: For this question you need `Orders`, `Customers` and `Order Details`.
