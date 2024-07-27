import tkinter as tk
from tkinter import messagebox


class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = {}
        self.contact_id = 0

        self.setup_ui()

    def setup_ui(self):
        # Add contact fields
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Phone").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Address").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1)

        # Add contact button
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)

        # View contacts button
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2)

        # Search contact
        tk.Label(self.root, text="Search by Name/Phone").grid(row=6, column=0)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=6, column=1)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=7, column=0, columnspan=2)

        # Update and delete contact
        tk.Label(self.root, text="Contact ID for Update/Delete").grid(row=8, column=0)
        self.contact_id_entry = tk.Entry(self.root)
        self.contact_id_entry.grid(row=8, column=1)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=9, column=0, columnspan=2)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=10, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[self.contact_id] = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            self.contact_id += 1
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required!")

    def view_contacts(self):
        contacts_str = "ID | Name | Phone\n"
        contacts_str += "-" * 30 + "\n"
        for cid, info in self.contacts.items():
            contacts_str += f"{cid} | {info['name']} | {info['phone']}\n"

        messagebox.showinfo("Contacts", contacts_str)

    def search_contact(self):
        query = self.search_entry.get()
        result_str = "ID | Name | Phone\n"
        result_str += "-" * 30 + "\n"
        for cid, info in self.contacts.items():
            if query in info['name'] or query in info['phone']:
                result_str += f"{cid} | {info['name']} | {info['phone']}\n"

        if result_str.strip() == "ID | Name | Phone\n" + "-" * 30:
            result_str = "No contacts found."

        messagebox.showinfo("Search Results", result_str)

    def update_contact(self):
        contact_id = self.contact_id_entry.get()
        if contact_id.isdigit() and int(contact_id) in self.contacts:
            contact_id = int(contact_id)
            self.contacts[contact_id]['name'] = self.name_entry.get()
            self.contacts[contact_id]['phone'] = self.phone_entry.get()
            self.contacts[contact_id]['email'] = self.email_entry.get()
            self.contacts[contact_id]['address'] = self.address_entry.get()
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Contact ID not found!")

    def delete_contact(self):
        contact_id = self.contact_id_entry.get()
        if contact_id.isdigit() and int(contact_id) in self.contacts:
            contact_id = int(contact_id)
            del self.contacts[contact_id]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Contact ID not found!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_id_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
