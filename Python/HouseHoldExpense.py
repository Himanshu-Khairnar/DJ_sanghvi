import json
from datetime import datetime
from functools import reduce


class Expense:
    def __init__(self, date, description, category, amount, who_paid):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.description = description
        self.category = category
        self.amount = float(amount)
        self.who_paid = who_paid

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "category": self.category,
            "amount": self.amount,
            "who_paid": self.who_paid
        }


class ExpenseBook:
    def __init__(self, filename="expenses.json", budget=50000):
        self.filename = filename
        self.budget = budget
        self.expenses = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.expenses = [Expense(**e) for e in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=4)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_data()
        self.check_budget()

    def edit_expense(self, index, new_expense):
        if 0 <= index < len(self.expenses):
            self.expenses[index] = new_expense
            self.save_data()

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_data()

    def search_by_description(self, keyword):
        return list(filter(lambda e: keyword.lower() in e.description.lower(), self.expenses))

    def filter_by_category(self, category):
        return list(filter(lambda e: e.category.lower() == category.lower(), self.expenses))

    def filter_by_person(self, person):
        return list(filter(lambda e: e.who_paid.lower() == person.lower(), self.expenses))

    def filter_by_date_range(self, start, end):
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
        return list(filter(lambda e: start <= e.date <= end, self.expenses))

    def total_spending(self):
        return reduce(lambda acc, e: acc + e.amount, self.expenses, 0)

    def average_spending(self):
        return self.total_spending() / len(self.expenses) if self.expenses else 0

    def expenses_as_dicts(self):
        return list(map(lambda e: e.to_dict(), self.expenses))

    def category_totals(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def top_categories(self, n=3):
        sorted_cats = sorted(self.category_totals().items(), key=lambda x: x[1], reverse=True)
        return sorted_cats[:n]

    def outliers(self, threshold=5000):
        return list(filter(lambda e: e.amount > threshold, self.expenses))

    def sort_by_date(self):
        self.expenses.sort(key=lambda e: e.date)

    def sort_by_amount(self):
        self.expenses.sort(key=lambda e: e.amount, reverse=True)

    def check_budget(self):
        total = self.total_spending()
        if total > self.budget:
            print(f"\n⚠️ Warning: Budget exceeded! Total spent = {total}, Budget = {self.budget}\n")


def menu():
    book = ExpenseBook()

    while True:
        print("\n--- Household Expense Tracker ---")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. View All Expenses")
        print("5. Filter/Search Expenses")
        print("6. Analyze & Summarize Spending")
        print("7. Sort Expenses")
        print("8. Export Data")
        print("9. Exit & Save")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            desc = input("Description: ")
            cat = input("Category: ")
            amt = input("Amount: ")
            who = input("Who paid: ")
            book.add_expense(Expense(date, desc, cat, amt, who))
            print("✅ Expense added.")

        elif choice == "2":
            for i, e in enumerate(book.expenses):
                print(i, e.to_dict())
            idx = int(input("Enter index to edit: "))
            date = input("New Date (YYYY-MM-DD): ")
            desc = input("New Description: ")
            cat = input("New Category: ")
            amt = input("New Amount: ")
            who = input("New Who paid: ")
            book.edit_expense(idx, Expense(date, desc, cat, amt, who))
            print("✏️ Expense updated.")

        elif choice == "3":
            for i, e in enumerate(book.expenses):
                print(i, e.to_dict())
            idx = int(input("Enter index to delete: "))
            book.delete_expense(idx)
            print("🗑️ Expense deleted.")

        elif choice == "4":
            for i, e in enumerate(book.expenses):
                print(i, e.to_dict())

        elif choice == "5":
            print("a. Filter by Category")
            print("b. Filter by Person")
            print("c. Search by Description")
            print("d. Filter by Date Range")
            sub = input("Choose option: ")

            if sub == "a":
                cat = input("Enter category: ")
                results = book.filter_by_category(cat)
            elif sub == "b":
                person = input("Enter person: ")
                results = book.filter_by_person(person)
            elif sub == "c":
                keyword = input("Enter keyword: ")
                results = book.search_by_description(keyword)
            elif sub == "d":
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")
                results = book.filter_by_date_range(start, end)
            else:
                results = []

            for r in results:
                print(r.to_dict())

        elif choice == "6":
            print("Total Spending:", book.total_spending())
            print("Average Spending:", book.average_spending())
            print("Category Totals:", book.category_totals())
            print("Top Categories:", book.top_categories())
            print("Outliers:", [o.to_dict() for o in book.outliers()])

        elif choice == "7":
            print("a. Sort by Date")
            print("b. Sort by Amount")
            sub = input("Choose option: ")
            if sub == "a":
                book.sort_by_date()
            elif sub == "b":
                book.sort_by_amount()
            print("✅ Sorted.")

        elif choice == "8":
            data = book.expenses_as_dicts()
            with open("expenses_export.json", "w") as f:
                json.dump(data, f, indent=4)
            print("📁 Data exported to expenses_export.json")

        elif choice == "9":
            book.save_data()
            print("💾 Data saved. Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    menu()
