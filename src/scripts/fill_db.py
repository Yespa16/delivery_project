import csv
import requests

API_URL = "http://127.0.0.1:8000"

COMPANIES_CSV   = "companies.csv"
PRODUCTS_CSV    = "products.csv"
DELIVERIES_CSV  = "deliveries.csv"

def fill_companies_from_csv():
  with open(COMPANIES_CSV, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      company = {
          "name": row["name"],
          "workers_cnt": int(row["workers_cnt"]),
          "area": row["area"],
      }
      response = requests.post(f"{API_URL}/company/", json=company)
      print(f"{company['name']}: {response.status_code}")


def fill_products_from_csv():
  with open(PRODUCTS_CSV, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      product = {
          "name": row["name"],
          "expr_date": row["expr_date"],
          "cost": float(row["cost"]),
          "unit": row["unit"]
      }
      response = requests.post(f"{API_URL}/product/", json=product)
      print(f"{product['name']}: {response.status_code}")


def fill_deliveries_from_csv():
  with open(DELIVERIES_CSV, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      delivery = {
          "price": float(row["price"]),
          "date": row["date"],
          "volume": float(row["volume"]),
          "company_id": int(row["company_id"]),
          "product_id": int(row["product_id"]),
      }
      response = requests.post(f"{API_URL}/delivery/", json=delivery)
      print(f"Delivery for company_id {delivery['company_id']} and product_id {delivery['product_id']}: {response.status_code}")


if __name__ == "__main__":
  fill_companies_from_csv()
  fill_products_from_csv()
  fill_deliveries_from_csv()
  print("The DB was filled")