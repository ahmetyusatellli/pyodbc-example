# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Wed Jul 12 12:52:37 2017

@author: Admin
"""
import pyodbc
#row diyince tek satır bastırıyor.row[0] diyince tek satırın ilk
#column u bastırıyor. rows diyince tüm herşeyi bastırıyor. rows[0]
#diyince ilk satırdaki tüm bilgileri bastırıyor.


def printTable(row,rows):
    #print(rows)
    for row in rows:
        print(row)
   
def get_address(cursor):
    cursor.execute("""SELECT top 10 [AddressID]
                            ,[AddressLine1]
                            ,[AddressLine2]
                            ,[City]
                            ,[StateProvince]
                            ,[CountryRegion]
                            ,[PostalCode]
                       FROM  [SalesLT].[Address]""")
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print("\t\t\t*-- ADDRESS LIST --*")
    printTable(row,rows)


def get_customers(cursor):
    cursor.execute("""SELECT top 10 [CustomerID]
                             ,[FirstName]
                             ,[LastName]
                             ,[CompanyName]
                             ,[SalesPerson]
                             ,[EmailAddress]
                             ,[Phone]
                         FROM [SalesLT].[Customer]""")
    row = cursor.fetchone()
    rows = cursor.fetchall()
    
    print("\t\t\t*-- CUSTOMERS LIST --*")

    printTable(row,rows)
        
    
def customers_address(cursor):    
    cursor.execute("""SELECT top 10  CA.[CustomerID],
                        		CA.[AddressID],
		                        C.[FirstName],
                         		C.[LastName],
                               C.[CompanyName],
                        		A.[City],
                        		A.[CountryRegion]
                    FROM [SalesLT].[CustomerAddress] CA
                    INNER JOIN [SalesLT].[Customer] C ON CA.CustomerID = C.CustomerID
                    INNER JOIN [SalesLT].[Address] AS A ON A.AddressID = CA.AddressID  
                    """)
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print("\t\t\t*-- CUSTOMERS' ADDRESS LIST --*")
    printTable(row,rows)
    
    
def get_product(cursor):
    cursor.execute("""  SELECT TOP 10 [ProductID]
                              ,[Name]
                              ,[StandardCost]
                              ,[ListPrice]
                              ,[ProductCategoryID]
                              ,[ProductModelID]
                          FROM [SalesLT].[Product]
                          """)    
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print("\t\t\t*-- PRODUCT LIST --*")
    printTable(row,rows)  
    
def product_category(cursor):
    cursor.execute(""" SELECT TOP 10  p.[ProductID],
		                        p.[Name],
		                        pc.[ProductCategoryID],
		                        pm.[ProductModelID],
	                         	p.[StandardCost],
	                         	p.[ListPrice]

                        FROM [SalesLT].[Product] AS p
INNER JOIN [SalesLT].[ProductModel] AS pm ON p.ProductModelID = pm.ProductModelID
INNER JOIN [SalesLT].[ProductCategory] AS pc on p.ProductCategoryID = pc.ProductCategoryID
                   """)    
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print("\t\t\t*-- PRODUCT CATEGORY LIST --*")
    printTable(row,rows)  
    
def product_discription(cursor):
    cursor.execute("""SELECT TOP 10   pd.[ProductModelID],
			                        	pd.[ProductDescriptionID],
				                        pm.[Name],
			                  	       pd.[Culture],
				                         p.[Description]				

                      FROM [SalesLT].[ProductModelProductDescription] AS pd
INNER JOIN [SalesLT].[ProductModel] AS pm ON pm.ProductModelID = pd.ProductModelID
INNER JOIN [SalesLT].[ProductDescription] AS p ON p.ProductDescriptionID = pd.ProductDescriptionID
ORDER BY pd.[ProductDescriptionID]              
                   """)    
    
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print("\t\t\t*-- PRODUCT DISCRIPTION LIST --*")
    printTable(row,rows)  

def salesOrderDetail(cursor):
    cursor.executr("""SELECT TOP 10 SD.[SalesOrderID],
		SD.[SalesOrderDetailID],
		SD.[ProductID],
		SD.[UnitPrice],
		SH.[SalesOrderNumber],
		SH.[ShipMethod],
		SH.[SubTotal]

  FROM [SalesLT].[SalesOrderDetail] AS SD
  INNER JOIN [SalesLT].[SalesOrderHeader] AS SH ON SH.SalesOrderID = SD.SalesOrderID
                   """)
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print("\t\t\t*-- SALES ORDER DETAIL --*")
    printTable(row,rows)  
    
def main():
    server = 'yusasqlserver.database.windows.net' #database server
    database = 'YusaDb'#database name
    username = 'yusa'
    password = '123456aA'
    driver= '{ODBC Driver 13 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    
    cont = 'c'
    print('Welcome to Databases')
    while (cont != 'e') or(cont != 'E') :
        print("""
        What would you like to do ?
        1 - Address List
        2 - Customer List
        3 - Customer's Address List
        4 - Product List
        5 - Product Category
        6 - Product Description
        7 - Sales Order Detail
        """)
        choice = input("select an option > ")
        print(type(choice))
        #choice = int(choice)
        if choice > 8 or choice < 1:
            print ("WRONG CHOISE")
        if int(choice) == 1:
            get_address(cursor)
        elif int(choice) == 2:
            get_customers(cursor)
        elif int(choice) == 3:
            customers_address(cursor)     
        elif int(choice) == 4:
            get_product(cursor)
        elif int(choice) == 5:
            product_category(cursor)
        elif int(choice) == 6:
            product_discription(cursor)
        else:
            print ("WRONG CHOISE")
            
        cont = input('IF YOU WANT TO EXIT PRESS "E"\n')
        #print(cont)
        if (cont == 'e') or (cont == 'E'):
            break
        
if __name__ == '__main__':
    main()
