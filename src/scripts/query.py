import requests
from datetime import datetime

# API endpoint
API_URL = "http://127.0.0.1:8000/"

def select(product_name):
  url = f"{API_URL}product/?product_name={product_name}"
  response = requests.get(url)
  if response.status_code != 200:
    return
  products = response.json()
  expired_products = [product for product in products if product["unit"] == "kg" and product["cost"] < 100]
  return expired_products


def join(company, product):
  delivery_url = f"{API_URL}delivery/?company_name={company}"
  delivery_response = requests.get(delivery_url)
  if delivery_response.status_code != 200:
    print("Delivery API Call failed")
    return {"Message": "Failed"}
  deliveries = delivery_response.json()
  
  product_url = f"{API_URL}product/?product_name={product}"
  product_response = requests.get(product_url)
  if product_response.status_code != 200:
    print("Product API call failed!")
    return {"Message": "Failed"}
  products = product_response.json()
  product_ids = [product["id"] for product in products]
  result = [delivery for delivery in deliveries if delivery["product_id"] in product_ids]
  
  return len(result)



def update():
  products_url = f"{API_URL}products/"
  products_response = requests.get(products_url)
  if products_response.status_code != 200:
    print(f"Products API call failed, status code: {products_response.status_code}")
    return
  products = products_response.json()
  
  for product in products:
    expr_date = datetime.strptime(product["expr_date"], "%Y-%m-%d").date()
    today = datetime.now().date()
    if expr_date < today:      
      update_url = f"{API_URL}product/{product['id']}"
      payload = {
        "name": product["name"],
        "expr_date": product["expr_date"],
        "cost": product["cost"] * 0.5,
        "unit": product["unit"],
        "description": {"additional_desc":"This item was updated"}
      }
      update_response = requests.put(update_url, json=payload)
      if update_response.status_code != 200:
        print(f"Update API call failed, status: {update_response.status_code}")
      return update_response.json()


def group_by():
  group_url = f"{API_URL}company/grouped/"
  response = requests.get(group_url)
  if response.status_code != 200:
    print("Group By API call failed")
    return
  return response.json()



def sort(field, order):
  sort_url = f"{API_URL}products/?sort_by={field}&order={order}"
  response = requests.get(sort_url)
  if response.status_code != 200:
    print("Sort API CALL Failed")
    return
  return response.json()


if __name__ == '__main__':
  print("Starting SELECT query")
  print(select("Product 2"))
  
  print("Starting JOIN query")
  print(join("Company2", "Product 2"))
  
  print("Starting UPDATE query")
  print(update())

  print("Starting GROUP BY query")
  print(group_by())
  
  print("Starting SORT query")
  print(sort("cost", "asc"))