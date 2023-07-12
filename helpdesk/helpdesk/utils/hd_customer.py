import frappe

def clear_data():
    delete_all_hd_customer()

def delete_all_hd_customer():
    for hdc in frappe.get_list("HD Customer"):
        hd_customer = frappe.get_doc("HD Customer", hdc.name)

        hd_customer.delete()
        frappe.db.commit()

def create_hd_customer_from_customer():
    
    for c in frappe.get_list("Customer"):
        customer = frappe.get_doc("Customer", c.name)
        new_hd_customer = frappe.new_doc("HD Customer")
        new_hd_customer.customer_name = customer.name
        new_hd_customer.domain = customer.territory
        new_hd_customer.woocommerce_email = customer.woocommerce_email
        new_hd_customer.erp_customer = customer.name

        new_hd_customer.insert(ignore_permissions=True)

        frappe.db.commit()
