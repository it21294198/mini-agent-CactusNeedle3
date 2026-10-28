import needle
import requests


@needle.tool
def get_products(limit: int = 5):
    """Retrieve products from the Fake Store API.

    Args:
        limit: Maximum number of products to retrieve.
    """
    if not 1 <= limit <= 20:
        return {"error": "Limit must be between 1 and 20."}

    response = requests.get(
        "https://fakestoreapi.com/products",
        params={"limit": limit},
        timeout=10
    )

    response.raise_for_status()

    products = response.json()

    return [
        {
            "id": p["id"],
            "title": p["title"],
            "price": p["price"],
            "category": p["category"]
        }
        for p in products
    ]


agent = needle.Needle(tools=[get_products])

result = agent.run(
    "Show me five products and their prices."
)

print(result["results"])
