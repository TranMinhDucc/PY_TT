from pymongo import MongoClient


def setup_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["online_store"]

    if "products" not in db.list_collection_names():
        db.create_collection("products")
    if "orders" not in db.list_collection_names():
        db.create_collection("orders")

    print("Database và collections đã sẵn sàng.")
    return db


def add_data(db):
    products = db.products
    orders = db.orders

    product_list = [
        {"product_id": "SP001", "name": "Áo thun", "price": 150000.0, "stock": 50},
        {"product_id": "SP002", "name": "Quần jeans",
            "price": 300000.0, "stock": 30},
        {"product_id": "SP003", "name": "Giày sneaker",
            "price": 500000.0, "stock": 20},
        {"product_id": "SP004", "name": "Áo sơ mi", "price": 250000.0, "stock": 40},
        {"product_id": "SP005", "name": "Túi xách", "price": 400000.0, "stock": 10},
    ]
    products.insert_many(product_list)

    order_list = [
        {"order_id": "DH001", "customer_name": "An", "product_id": "SP001",
            "quantity": 2, "total_price": 300000.0, "order_date": "2025-04-11"},
        {"order_id": "DH002", "customer_name": "Bình", "product_id": "SP002",
            "quantity": 1, "total_price": 300000.0, "order_date": "2025-04-12"},
        {"order_id": "DH003", "customer_name": "An", "product_id": "SP003",
            "quantity": 2, "total_price": 1000000.0, "order_date": "2025-04-13"},
        {"order_id": "DH004", "customer_name": "Cường", "product_id": "SP004",
            "quantity": 3, "total_price": 750000.0, "order_date": "2025-04-14"},
        {"order_id": "DH005", "customer_name": "Bình", "product_id": "SP005",
            "quantity": 1, "total_price": 400000.0, "order_date": "2025-04-15"},
        {"order_id": "DH006", "customer_name": "Cường", "product_id": "SP001",
            "quantity": 4, "total_price": 600000.0, "order_date": "2025-04-16"},
        {"order_id": "DH007", "customer_name": "An", "product_id": "SP002",
            "quantity": 1, "total_price": 300000.0, "order_date": "2025-04-17"},
        {"order_id": "DH008", "customer_name": "An", "product_id": "SP005",
            "quantity": 2, "total_price": 800000.0, "order_date": "2025-04-18"},
        {"order_id": "DH009", "customer_name": "Cường", "product_id": "SP003",
            "quantity": 1, "total_price": 500000.0, "order_date": "2025-04-19"},
        {"order_id": "DH010", "customer_name": "Bình", "product_id": "SP004",
            "quantity": 2, "total_price": 500000.0, "order_date": "2025-04-20"},
    ]
    orders.insert_many(order_list)

    print("Đã thêm dữ liệu mẫu.")


def query_orders(db, customer_name):
    print(f"Đơn hàng của {customer_name}:")
    orders = db.orders.find({
        "customer_name": customer_name,
        "total_price": {"$gt": 500000}
    }).sort("total_price", -1).limit(5)

    for order in orders:
        print(
            f"- Mã đơn: {order['order_id']}, Sản phẩm: {order['product_id']}, Tổng: {order['total_price']} VNĐ")


def update_order(db, order_id, new_quantity):
    order = db.orders.find_one({"order_id": order_id})
    product = db.products.find_one({"product_id": order["product_id"]})

    if order and product:
        new_total = new_quantity * product["price"]
        db.orders.update_one(
            {"order_id": order_id},
            {"$set": {"quantity": new_quantity, "total_price": new_total}}
        )
        print(
            f"Đã cập nhật đơn hàng {order_id} với số lượng {new_quantity} và tổng tiền {new_total} VNĐ.")


def delete_order(db):
    result = db.orders.delete_many({"total_price": {"$lt": 100000}})
    print(
        f" Đã xoá {result.deleted_count} đơn hàng có tổng giá trị dưới 100000 VNĐ.")


def generate_report(db):
    print("Báo cáo cửa hàng:")

    pipeline = [
        {"$group": {"_id": "$product_id", "total_revenue": {"$sum": "$total_price"}}}
    ]
    revenues = db.orders.aggregate(pipeline)
    for item in revenues:
        print(
            f"- Sản phẩm {item['_id']}: Doanh thu {item['total_revenue']} VNĐ")

    low_stock_count = db.products.count_documents({"stock": {"$lt": 10}})
    print(f"- Sản phẩm tồn kho thấp: {low_stock_count} sản phẩm")


def cleanup_database(db):
    if "orders" in db.list_collection_names():
        confirm = input("Bạn có muốn xoá collection 'orders'? (y/n): ").lower()
        if confirm == 'y':
            db.orders.drop()
            print(" Đã xoá collection 'orders'.")


def main():
    db = setup_database()
    add_data(db)
    query_orders(db, "An")
    update_order(db, "DH001", 3)
    delete_order(db)
    generate_report(db)
    cleanup_database(db)


if __name__ == "__main__":
    main()
