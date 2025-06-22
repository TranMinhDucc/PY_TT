import numpy as np

events = [
    {"id": "EV001", "name": "Hội chợ sách",
        "ticket_price": 50000.0, "tickets_left": 200},
    {"id": "EV002", "name": "Triển lãm tranh",
        "ticket_price": 80000.0, "tickets_left": 150},
    {"id": "EV003", "name": "Workshop làm gốm",
        "ticket_price": 120000.0, "tickets_left": 50},
    {"id": "EV004", "name": "Hội chợ ẩm thực",
        "ticket_price": 60000.0, "tickets_left": 30},
    {"id": "EV005", "name": "Triển lãm công nghệ",
        "ticket_price": 100000.0, "tickets_left": 80}
]

sponsors = {
    "SP001": ("Công ty A", 5000000.0),
    "SP002": ("Tập đoàn B", 10000000.0),
    "SP003": ("Doanh nghiệp C", 3000000.0)
}


def manage_events():
    def add_event(event):
        events.append(event)

    def delete_event(event_id):
        global events
        events = [e for e in events if e["id"] != event_id]

    def update_tickets(event_id, new_ticket_count):
        for e in events:
            if e["id"] == event_id:
                e["tickets_left"] = new_ticket_count
                return
        print("Không tìm thấy sự kiện.")

    def get_event(event_id):
        for e in events:
            if e["id"] == event_id:
                print(e)
                return
        print("Không tìm thấy sự kiện.")

    def list_events():
        for e in events:
            print(e)

    def average_ticket_price():
        prices = np.array([e["ticket_price"] for e in events])
        print(f"Giá vé trung bình: {np.mean(prices)} VNĐ")

    return add_event, delete_event, update_tickets, get_event, list_events, average_ticket_price


def manage_sponsors():
    def add_sponsor(sponsor_id, name, amount):
        sponsors[sponsor_id] = (name, amount)

    def delete_sponsor(sponsor_id):
        sponsors.pop(sponsor_id, None)

    def update_sponsor_amount(sponsor_id, new_amount):
        if sponsor_id in sponsors:
            name, _ = sponsors[sponsor_id]
            sponsors[sponsor_id] = (name, new_amount)
        else:
            print("Không tìm thấy nhà tài trợ.")

    def get_sponsor(sponsor_id):
        print(sponsors.get(sponsor_id, "Không tìm thấy nhà tài trợ."))

    def list_sponsors():
        for k, v in sponsors.items():
            print(f"{k}: {v}")

    return add_sponsor, delete_sponsor, update_sponsor_amount, get_sponsor, list_sponsors


sold_event_ids = set()
ticket_history = []


def process_tickets():
    def sell_ticket(event_id, ticket_id, quantity):
        for e in events:
            if e["id"] == event_id:
                if e["tickets_left"] >= quantity:
                    e["tickets_left"] -= quantity
                    ticket_history.append({
                        "event_id": event_id,
                        "ticket_id": ticket_id,
                        "quantity": quantity
                    })
                    sold_event_ids.add(event_id)
                else:
                    print("Không đủ vé.")
                return
        print("Không tìm thấy sự kiện.")

    def check_event_sold(event_id):
        return event_id in sold_event_ids

    def list_tickets():
        for t in ticket_history:
            print(t)

    def remove_zero_quantity_tickets():
        global ticket_history
        ticket_history[:] = [t for t in ticket_history if t["quantity"] > 0]

    return sell_ticket, check_event_sold, list_tickets, remove_zero_quantity_tickets


def generate_report():
    low_ticket_events = [e["name"] for e in events if e["tickets_left"] < 20]

    total_value = np.sum([e["ticket_price"] * e["tickets_left"]
                         for e in events])

    sold_ids = set([t["event_id"] for t in ticket_history])

    print("Sự kiện sắp hết vé:", low_ticket_events)
    print("Tổng giá trị vé còn lại:", f"{total_value:,} VNĐ")
    print("Sự kiện đã bán vé:", list(sold_ids))


def main():
    add_event, delete_event, update_tickets, get_event, list_events, avg_price = manage_events()
    add_event({"id": "EV006", "name": "Chợ đêm văn hóa",
              "ticket_price": 40000.0, "tickets_left": 10})
    update_tickets("EV003", 45)

    add_sponsor, delete_sponsor, update_sponsor_amount, get_sponsor, list_sponsors = manage_sponsors()
    add_sponsor("SP004", "Tổ chức D", 2500000.0)
    get_sponsor("SP004")

    sell_ticket, check_sold, list_ticket_history, clean_tickets = process_tickets()
    sell_ticket("EV001", "TICKET_001", 10)
    sell_ticket("EV003", "TICKET_002", 5)

    generate_report()


if __name__ == "__main__":
    main()
